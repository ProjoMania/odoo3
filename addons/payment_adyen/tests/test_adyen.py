# -*- coding: utf-8 -*-

from lxml import objectify
import urllib.parse

from openerp.addons.payment.models.payment_acquirer import ValidationError
from openerp.addons.payment.tests.common import PaymentAcquirerCommon
from openerp.addons.payment_adyen.controllers.main import AdyenController
from openerp.osv.orm import except_orm
from openerp.tools import mute_logger


class AdyenCommon(PaymentAcquirerCommon):

    def setUp(self):
        super(AdyenCommon, self).setUp()
        cr, uid = self.cr, self.uid
        self.base_url = self.registry('ir.config_parameter').get_param(cr, uid, 'web.base.url')

        # get the adyen account
        model, self.adyen_id = self.registry('ir.model.data').get_object_reference(cr, uid, 'payment_adyen', 'payment_acquirer_adyen')

        # some CC (always use expiration date 06 / 2016, cvc 737, cid 7373 (amex))
        self.amex = (('370000000000002', '7373'))
        self.dinersclub = (('36006666333344', '737'))
        self.discover = (('6011601160116611', '737'), ('644564456445644', '737'))
        self.jcb = (('3530111333300000', '737'))
        self.mastercard = (('5555444433331111', '737'), ('5555555555554444', '737'))
        self.visa = (('4111 1111 1111 1111', '737'), ('4444333322221111', '737'))
        self.mcdebit = (('5500000000000004', '737'))
        self.visadebit = (('4400000000000008', '737'))
        self.maestro = (('6731012345678906', '737'))
        self.laser = (('630495060000000000', '737'))
        self.hipercard = (('6062828888666688', '737'))
        self.dsmastercard = (('521234567890 1234', '737', 'user', 'password'))
        self.dsvisa = (('4212345678901237', '737', 'user', 'password'))
        self.mistercash = (('6703444444444449', None, 'user', 'password'))


class AdyenServer2Server(AdyenCommon):

    def test_00_tx_management(self):
        cr, uid, context = self.cr, self.uid, {}


class AdyenForm(AdyenCommon):

    def test_10_adyen_form_render(self):
        cr, uid, context = self.cr, self.uid, {}
        # be sure not to do stupid things
        adyen = self.payment_acquirer.browse(self.cr, self.uid, self.adyen_id, None)
        self.assertEqual(adyen.environment, 'test', 'test without test environment')

        # ----------------------------------------
        # Test: button direct rendering
        # ----------------------------------------

        form_values = {
            'merchantAccount': 'OpenERPCOM',
            'merchantReference': 'test_ref0',
            'skinCode': 'cbqYWvVL',
            'paymentAmount': '1',
            'currencyCode': 'EUR',
            'resURL': '%s' % urllib.parse.urljoin(self.base_url, AdyenController._return_url),
        }

        # render the button
        res = self.payment_acquirer.render(
            cr, uid, self.adyen_id,
            'test_ref0', 0.01, self.currency_euro_id,
            partner_id=None,
            partner_values=self.buyer_values,
            context=context)

        # check form result
        tree = objectify.fromstring(res)
        self.assertEqual(tree.get('action'), 'https://test.adyen.com/hpp/pay.shtml', 'adyen: wrong form POST url')
        for form_input in tree.input:
            if form_input.get('name') in ['submit', 'shipBeforeDate', 'sessionValidity', 'shopperLocale', 'merchantSig']:
                continue
            self.assertEqual(
                form_input.get('value'),
                form_values[form_input.get('name')],
                'adyen: wrong value for input %s: received %s instead of %s' % (form_input.get('name'), form_input.get('value'), form_values[form_input.get('name')])
            )

    # @mute_logger('openerp.addons.payment_adyen.models.adyen', 'ValidationError')
    # def test_20_paypal_form_management(self):
    #     cr, uid, context = self.cr, self.uid, {}
    #     # be sure not to do stupid things
    #     adyen = self.payment_acquirer.browse(self.cr, self.uid, self.adyen_id, None)
    #     self.assertEqual(adyen.env, 'test', 'test without test env')

# {'authResult': u'AUTHORISED',
#  'merchantReference': u'SO014',
#  'merchantReturnData': u'return_url=/shop/payment/validate',
#  'merchantSig': u'GaLRO8aMHFaQX3gQ5BVP/YETzeA=',
#  'paymentMethod': u'visa',
#  'pspReference': u'8813859935907337',
#  'shopperLocale': u'en_US',
#  'skinCode': u'cbqYWvVL'}