import dns
import sys
from multiprocessing.dummy import Pool as ThreadPool

UNWATED_DOMAINS = ['hotmail', 'live', 'gmx', 'outlook', 'gmail', 'googlemail', 'yahoo', 'msn', 'aol', 'gmx', 'ymail']
def SET(Combo):
	LOOKUP = dns.resolver.query(Combo.split(":")[0].split("@")[1], 'MX')
	SET = str(set(LOOKUP))
	
	return SET

def Run(Combo):
	
		
		try:	
			Comboa = Combo.split(":")[0].split("@")[1].split(".")[0]
			if Comboa in UNWATED_DOMAINS:
				pass
			else :
				if 'outlook.com' in SET(Combo):
					File_Office365 = open('office365.txt', 'a')
					File_Office365.write(Combo + '\n')
					File_Office365.close()
				elif 'secureserver.net' in SET(Combo):
					File_GoDaddy = open('godaddy.txt', 'a')
					File_GoDaddy.write(Combo + '\n')
					File_GoDaddy.close()
				elif 'emailsrvr.com' in SET(Combo):
					File_Rackspace = open('rackspace.txt', 'a')
					File_Rackspace.write(Combo + '\n')
					File_Rackspace.close()
				elif 'google.com' in SET(Combo):
					File_Gsuite = open('gsuite.txt', 'a')
					File_Gsuite.write(Combo + '\n')
					File_Gsuite.close()
				elif 'ovh' in SET(Combo):
					File_ovh = open('ovh.txt', 'a')
					File_ovh.write(Combo + '\n')
					File_ovh.close()
				elif 'iobox' in SET(Combo):
					File_iobox = open('iobox.txt', 'a')
					File_iobox.write(Combo + '\n')
					File_iobox.close()
				elif 'cuida' in SET(Combo):
					File_cuida = open('cuida.txt', 'a')
					File_cuida.write(Combo + '\n')
					File_cuida.close()
				elif 'hostek' in SET(Combo):
					File_hostek = open('hostek.txt', 'a')
					File_hostek.write(Combo + '\n')
					File_hostek.close()
				elif 'spambox' in SET(Combo):
					File_spambox = open('spambox.txt', 'a')
					File_spambox.write(Combo + '\n')
					File_spambox.close()
				elif 'spespamboxcoza' in SET(Combo):
					File_spespamboxcoza = open('spespamboxcoza.txt', 'a')
					File_spespamboxcoza.write(Combo + '\n')
					File_spespamboxcoza.close()
				elif 'uceboxcoza' in SET(Combo):
					File_uceboxcoza = open('uceboxcoza.txt', 'a')
					File_uceboxcoza.write(Combo + '\n')
					File_uceboxcoza.close()
				elif 'ucebox' in SET(Combo):
					File_ucebox = open('ucebox.txt', 'a')
					File_ucebox.write(Combo + '\n')
					File_ucebox.close()
				elif 'mxhichina' in SET(Combo):
					File_mxhichina = open('mxhichina.txt', 'a')
					File_mxhichina.write(Combo + '\n')
					File_mxhichina.close()
				elif 'prosites' in SET(Combo):
					File_prosites = open('prosites.txt', 'a')
					File_prosites.write(Combo + '\n')
					File_prosites.close()
				elif 'argewebhosting' in SET(Combo):
					File_argewebhosting = open('argewebhosting.txt', 'a')
					File_argewebhosting.write(Combo + '\n')
					File_argewebhosting.close()
				elif 'serviciodecorreo' in SET(Combo):
					File_serviciodecorreo = open('serviciodecorreo.txt', 'a')
					File_serviciodecorreo.write(Combo + '\n')
					File_serviciodecorreo.close()
				elif 'romtelecom' in SET(Combo):
					File_romtelecom = open('romtelecom.txt', 'a')
					File_romtelecom.write(Combo + '\n')
					File_romtelecom.close()
				elif 'register' in SET(Combo):
					File_register = open('register.txt', 'a')
					File_register.write(Combo + '\n')
					File_register.close()
				elif 'arubabusiness' in SET(Combo):
					File_arubabusiness = open('arubabusiness.txt', 'a')
					File_arubabusiness.write(Combo + '\n')
					File_arubabusiness.close()
				elif 'widestore' in SET(Combo):
					File_widestore = open('widestore.txt', 'a')
					File_widestore.write(Combo + '\n')
					File_widestore.close()
				elif 'ik2' in SET(Combo):
					File_ik2 = open('ik2.txt', 'a')
					File_ik2.write(Combo + '\n')
					File_ik2.close()
				elif 'accountservergroup' in SET(Combo):
					File_accountservergroup = open('accountservergroup.txt', 'a')
					File_accountservergroup.write(Combo + '\n')
					File_accountservergroup.close()
				elif 'exchangedefender' in SET(Combo):
					File_exchangedefender = open('exchangedefender.txt', 'a')
					File_exchangedefender.write(Combo + '\n')
					File_exchangedefender.close()
				elif 'ooredoo' in SET(Combo):
					File_ooredoo = open('ooredoo.txt', 'a')
					File_ooredoo.write(Combo + '\n')
					File_ooredoo.close()
				elif 'awinetworks' in SET(Combo):
					File_awinetworks = open('awinetworks.txt', 'a')
					File_awinetworks.write(Combo + '\n')
					File_awinetworks.close()
				elif 'vildmarksdata' in SET(Combo):
					File_vildmarksdata = open('vildmarksdata.txt', 'a')
					File_vildmarksdata.write(Combo + '\n')
					File_vildmarksdata.close()
				elif 'matrixsi' in SET(Combo):
					File_matrixsi = open('matrixsi.txt', 'a')
					File_matrixsi.write(Combo + '\n')
					File_matrixsi.close()
				elif 'antispamcloud' in SET(Combo):
					File_antispamcloud = open('antispamcloud.txt', 'a')
					File_antispamcloud.write(Combo + '\n')
					File_antispamcloud.close()
				elif 'bertramwireless' in SET(Combo):
					File_bertramwireless = open('bertramwireless.txt', 'a')
					File_bertramwireless.write(Combo + '\n')
					File_bertramwireless.close()
				elif 'jiransecurity' in SET(Combo):
					File_jiransecurity = open('jiransecurity.txt', 'a')
					File_jiransecurity.write(Combo + '\n')
					File_jiransecurity.close()
				elif 'cloudafrica' in SET(Combo):
					File_cloudafrica = open('cloudafrica.txt', 'a')
					File_cloudafrica.write(Combo + '\n')
					File_cloudafrica.close()
				elif 'relaypod' in SET(Combo):
					File_relaypod = open('relaypod.txt', 'a')
					File_relaypod.write(Combo + '\n')
					File_relaypod.close()
				elif 'spamgateway' in SET(Combo):
					File_spamgateway = open('spamgateway.txt', 'a')
					File_spamgateway.write(Combo + '\n')
					File_spamgateway.close()
				elif 'bnet' in SET(Combo):
					File_bnet = open('bnet.txt', 'a')
					File_bnet.write(Combo + '\n')
					File_bnet.close()
				elif 'natrohost' in SET(Combo):
					File_natrohost = open('natrohost.txt', 'a')
					File_natrohost.write(Combo + '\n')
					File_natrohost.close()
				elif 'cloudaccess' in SET(Combo):
					File_cloudaccess = open('cloudaccess.txt', 'a')
					File_cloudaccess.write(Combo + '\n')
					File_cloudaccess.close()
				elif 'viettelidc' in SET(Combo):
					File_viettelidc = open('viettelidc.txt', 'a')
					File_viettelidc.write(Combo + '\n')
					File_viettelidc.close()
				elif 'suantispam' in SET(Combo):
					File_suantispam = open('suantispam.txt', 'a')
					File_suantispam.write(Combo + '\n')
					File_suantispam.close()
				elif 'itb' in SET(Combo):
					File_itb = open('itb.txt', 'a')
					File_itb.write(Combo + '\n')
					File_itb.close()
				elif 'bomm' in SET(Combo):
					File_bomm = open('bomm.txt', 'a')
					File_bomm.write(Combo + '\n')
					File_bomm.close()
				elif 'mailcluster' in SET(Combo):
					File_mailcluster = open('mailcluster.txt', 'a')
					File_mailcluster.write(Combo + '\n')
					File_mailcluster.close()
				elif 'syrahost' in SET(Combo):
					File_syrahost = open('syrahost.txt', 'a')
					File_syrahost.write(Combo + '\n')
					File_syrahost.close()
				elif 'emirates' in SET(Combo):
					File_emirates = open('emirates.txt', 'a')
					File_emirates.write(Combo + '\n')
					File_emirates.close()
				elif 'gandi' in SET(Combo):
					File_gandi = open('gandi.txt', 'a')
					File_gandi.write(Combo + '\n')
					File_gandi.close()
				elif 'garantiserver' in SET(Combo):
					File_garantiserver = open('garantiserver.txt', 'a')
					File_garantiserver.write(Combo + '\n')
					File_garantiserver.close()
				elif 'net4india' in SET(Combo):
					File_net4india = open('net4india.txt', 'a')
					File_net4india.write(Combo + '\n')
					File_net4india.close()
				elif 'barracudanetworks' in SET(Combo):
					File_barracudanetworks = open('barracudanetworks.txt', 'a')
					File_barracudanetworks.write(Combo + '\n')
					File_barracudanetworks.close()
				elif 'spamprotection' in SET(Combo):
					File_spamprotection = open('spamprotection.txt', 'a')
					File_spamprotection.write(Combo + '\n')
					File_spamprotection.close()
				elif 'icoremail' in SET(Combo):
					File_icoremail = open('icoremail.txt', 'a')
					File_icoremail.write(Combo + '\n')
					File_icoremail.close()
				elif 'ocrpease' in SET(Combo):
					File_ocrpease = open('ocrpease.txt', 'a')
					File_ocrpease.write(Combo + '\n')
					File_ocrpease.close()
				elif 'icoremail' in SET(Combo):
					File_icoremail = open('icoremail.txt', 'a')
					File_icoremail.write(Combo + '\n')
					File_icoremail.close()
				elif 'netease' in SET(Combo):
					File_netease = open('netease.txt', 'a')
					File_netease.write(Combo + '\n')
					File_netease.close()
				elif 'gullestrupnet' in SET(Combo):
					File_gullestrupnet = open('gullestrupnet.txt', 'a')
					File_gullestrupnet.write(Combo + '\n')
					File_gullestrupnet.close()
				elif 'viaduc' in SET(Combo):
					File_viaduc = open('viaduc.txt', 'a')
					File_viaduc.write(Combo + '\n')
					File_viaduc.close()
				elif 'cnet' in SET(Combo):
					File_cnet = open('cnet.txt', 'a')
					File_cnet.write(Combo + '\n')
					File_cnet.close()
				elif 'macbay' in SET(Combo):
					File_macbay = open('macbay.txt', 'a')
					File_macbay.write(Combo + '\n')
					File_macbay.close()
				elif 'hostrocket' in SET(Combo):
					File_hostrocket = open('hostrocket.txt', 'a')
					File_hostrocket.write(Combo + '\n')
					File_hostrocket.close()
				elif 'serverdata' in SET(Combo):
					File_serverdata = open('serverdata.txt', 'a')
					File_serverdata.write(Combo + '\n')
					File_serverdata.close()
				elif 'iinet' in SET(Combo):
					File_iinet = open('iinet.txt', 'a')
					File_iinet.write(Combo + '\n')
					File_iinet.close()
				elif 'doteasy' in SET(Combo):
					File_doteasy = open('doteasy.txt', 'a')
					File_doteasy.write(Combo + '\n')
					File_doteasy.close()
				elif 'stackmail' in SET(Combo):
					File_stackmail = open('stackmail.txt', 'a')
					File_stackmail.write(Combo + '\n')
					File_stackmail.close()
				elif 'busgateway' in SET(Combo):
					File_busgateway = open('busgateway.txt', 'a')
					File_busgateway.write(Combo + '\n')
					File_busgateway.close()
				elif 'megaoffice' in SET(Combo):
					File_megaoffice = open('megaoffice.txt', 'a')
					File_megaoffice.write(Combo + '\n')
					File_megaoffice.close()
				elif 'foresttek' in SET(Combo):
					File_foresttek = open('foresttek.txt', 'a')
					File_foresttek.write(Combo + '\n')
					File_foresttek.close()
				elif 'lanaco' in SET(Combo):
					File_lanaco = open('lanaco.txt', 'a')
					File_lanaco.write(Combo + '\n')
					File_lanaco.close()
				elif 'lh' in SET(Combo):
					File_lh = open('lh.txt', 'a')
					File_lh.write(Combo + '\n')
					File_lh.close()
				elif 'nitrado' in SET(Combo):
					File_nitrado = open('nitrado.txt', 'a')
					File_nitrado.write(Combo + '\n')
					File_nitrado.close()
				elif 'fcomet' in SET(Combo):
					File_fcomet = open('fcomet.txt', 'a')
					File_fcomet.write(Combo + '\n')
					File_fcomet.close()
				elif 'supremebox' in SET(Combo):
					File_supremebox = open('supremebox.txt', 'a')
					File_supremebox.write(Combo + '\n')
					File_supremebox.close()
				elif 'globalprohosting' in SET(Combo):
					File_globalprohosting = open('globalprohosting.txt', 'a')
					File_globalprohosting.write(Combo + '\n')
					File_globalprohosting.close()
				elif 'localnet' in SET(Combo):
					File_localnet = open('localnet.txt', 'a')
					File_localnet.write(Combo + '\n')
					File_localnet.close()
				elif 'locaweb' in SET(Combo):
					File_locaweb = open('locaweb.txt', 'a')
					File_locaweb.write(Combo + '\n')
					File_locaweb.close()
				elif 'reflexion' in SET(Combo):
					File_reflexion = open('reflexion.txt', 'a')
					File_reflexion.write(Combo + '\n')
					File_reflexion.close()
				elif 'stsmail' in SET(Combo):
					File_stsmail = open('stsmail.txt', 'a')
					File_stsmail.write(Combo + '\n')
					File_stsmail.close()
				elif 'spamexperts' in SET(Combo):
					File_spamexperts = open('spamexperts.txt', 'a')
					File_spamexperts.write(Combo + '\n')
					File_spamexperts.close()
				elif 'netcore' in SET(Combo):
					File_netcore = open('netcore.txt', 'a')
					File_netcore.write(Combo + '\n')
					File_netcore.close()
				elif 'netpilot' in SET(Combo):
					File_netpilot = open('netpilot.txt', 'a')
					File_netpilot.write(Combo + '\n')
					File_netpilot.close()
				elif 'netregistry' in SET(Combo):
					File_netregistry = open('netregistry.txt', 'a')
					File_netregistry.write(Combo + '\n')
					File_netregistry.close()
				elif 'partnerconsole' in SET(Combo):
					File_partnerconsole = open('partnerconsole.txt', 'a')
					File_partnerconsole.write(Combo + '\n')
					File_partnerconsole.close()
				elif 'netsolmail' in SET(Combo):
					File_netsolmail = open('netsolmail.txt', 'a')
					File_netsolmail.write(Combo + '\n')
					File_netsolmail.close()
				elif 'mailgun' in SET(Combo):
					File_mailgun = open('mailgun.txt', 'a')
					File_mailgun.write(Combo + '\n')
					File_mailgun.close()
				elif 'dreamhost' in SET(Combo):
					File_dreamhost = open('dreamhost.txt', 'a')
					File_dreamhost.write(Combo + '\n')
					File_dreamhost.close()
				elif 'provisionmail' in SET(Combo):
					File_provisionmail = open('provisionmail.txt', 'a')
					File_provisionmail.write(Combo + '\n')
					File_provisionmail.close()
				elif 'nordnet' in SET(Combo):
					File_nordnet = open('nordnet.txt', 'a')
					File_nordnet.write(Combo + '\n')
					File_nordnet.close()
				elif 'wadax' in SET(Combo):
					File_wadax = open('wadax.txt', 'a')
					File_wadax.write(Combo + '\n')
					File_wadax.close()
				elif 'misp' in SET(Combo):
					File_misp = open('misp.txt', 'a')
					File_misp.write(Combo + '\n')
					File_misp.close()
				elif 'mailhostbox' in SET(Combo):
					File_mailhostbox = open('mailhostbox.txt', 'a')
					File_mailhostbox.write(Combo + '\n')
					File_mailhostbox.close()
				elif 'pioneerbroadband' in SET(Combo):
					File_pioneerbroadband = open('pioneerbroadband.txt', 'a')
					File_pioneerbroadband.write(Combo + '\n')
					File_pioneerbroadband.close()
				elif 'airmail' in SET(Combo):
					File_airmail = open('airmail.txt', 'a')
					File_airmail.write(Combo + '\n')
					File_airmail.close()
				elif 'everyone' in SET(Combo):
					File_everyone = open('everyone.txt', 'a')
					File_everyone.write(Combo + '\n')
					File_everyone.close()
				elif 'tophost' in SET(Combo):
					File_tophost = open('tophost.txt', 'a')
					File_tophost.write(Combo + '\n')
					File_tophost.close()
				elif 'dewaspamguard' in SET(Combo):
					File_dewaspamguard = open('dewaspamguard.txt', 'a')
					File_dewaspamguard.write(Combo + '\n')
					File_dewaspamguard.close()
				elif 'antispam' in SET(Combo):
					File_antispam = open('antispam.txt', 'a')
					File_antispam.write(Combo + '\n')
					File_antispam.close()
				elif 'redehost' in SET(Combo):
					File_redehost = open('redehost.txt', 'a')
					File_redehost.write(Combo + '\n')
					File_redehost.close()
				elif 'securemail' in SET(Combo):
					File_securemail = open('securemail.txt', 'a')
					File_securemail.write(Combo + '\n')
					File_securemail.close()
				elif 'oxito' in SET(Combo):
					File_oxito = open('oxito.txt', 'a')
					File_oxito.write(Combo + '\n')
					File_oxito.close()
				elif 'site' in SET(Combo):
					File_site = open('site.txt', 'a')
					File_site.write(Combo + '\n')
					File_site.close()
				elif 'orange' in SET(Combo):
					File_orange = open('orange.txt', 'a')
					File_orange.write(Combo + '\n')
					File_orange.close()
				elif 'inetwebusa' in SET(Combo):
					File_inetwebusa = open('inetwebusa.txt', 'a')
					File_inetwebusa.write(Combo + '\n')
					File_inetwebusa.close()
				elif 'stofanet' in SET(Combo):
					File_stofanet = open('stofanet.txt', 'a')
					File_stofanet.write(Combo + '\n')
					File_stofanet.close()
				elif 'msv1' in SET(Combo):
					File_msv1 = open('msv1.txt', 'a')
					File_msv1.write(Combo + '\n')
					File_msv1.close()
				elif 'mailinblack' in SET(Combo):
					File_mailinblack = open('mailinblack.txt', 'a')
					File_mailinblack.write(Combo + '\n')
					File_mailinblack.close()
				elif 'altospam' in SET(Combo):
					File_altospam = open('altospam.txt', 'a')
					File_altospam.write(Combo + '\n')
					File_altospam.close()
				elif 'ids33025' in SET(Combo):
					File_ids33025 = open('ids33025.txt', 'a')
					File_ids33025.write(Combo + '\n')
					File_ids33025.close()
				elif 'delosmail' in SET(Combo):
					File_delosmail = open('delosmail.txt', 'a')
					File_delosmail.write(Combo + '\n')
					File_delosmail.close()
				elif 'aswsp' in SET(Combo):
					File_aswsp = open('aswsp.txt', 'a')
					File_aswsp.write(Combo + '\n')
					File_aswsp.close()
				elif 'servadmin' in SET(Combo):
					File_servadmin = open('servadmin.txt', 'a')
					File_servadmin.write(Combo + '\n')
					File_servadmin.close()
				elif 'arkalone' in SET(Combo):
					File_arkalone = open('arkalone.txt', 'a')
					File_arkalone.write(Combo + '\n')
					File_arkalone.close()
				elif 'proserve' in SET(Combo):
					File_proserve = open('proserve.txt', 'a')
					File_proserve.write(Combo + '\n')
					File_proserve.close()
				elif 'iliane' in SET(Combo):
					File_iliane = open('iliane.txt', 'a')
					File_iliane.write(Combo + '\n')
					File_iliane.close()
				elif 'ipage' in SET(Combo):
					File_ipage = open('ipage.txt', 'a')
					File_ipage.write(Combo + '\n')
					File_ipage.close()
				elif 'softdebut' in SET(Combo):
					File_softdebut = open('softdebut.txt', 'a')
					File_softdebut.write(Combo + '\n')
					File_softdebut.close()
				elif 'vfemail' in SET(Combo):
					File_vfemail = open('vfemail.txt', 'a')
					File_vfemail.write(Combo + '\n')
					File_vfemail.close()
				elif 'exchangeadministrado' in SET(Combo):
					File_exchangeadministrado = open('exchangeadministrado.txt', 'a')
					File_exchangeadministrado.write(Combo + '\n')
					File_exchangeadministrado.close()
				elif 'fusemail' in SET(Combo):
					File_fusemail = open('fusemail.txt', 'a')
					File_fusemail.write(Combo + '\n')
					File_fusemail.close()
				elif 'logic' in SET(Combo):
					File_logic = open('logic.txt', 'a')
					File_logic.write(Combo + '\n')
					File_logic.close()
				elif 'watchtv' in SET(Combo):
					File_watchtv = open('watchtv.txt', 'a')
					File_watchtv.write(Combo + '\n')
					File_watchtv.close()
				elif 'site4now' in SET(Combo):
					File_site4now = open('site4now.txt', 'a')
					File_site4now.write(Combo + '\n')
					File_site4now.close()
				elif 'mijndomein' in SET(Combo):
					File_mijndomein = open('mijndomein.txt', 'a')
					File_mijndomein.write(Combo + '\n')
					File_mijndomein.close()
				elif 'zid' in SET(Combo):
					File_zid = open('zid.txt', 'a')
					File_zid.write(Combo + '\n')
					File_zid.close()
				elif 'torpig' in SET(Combo):
					File_torpig = open('torpig.txt', 'a')
					File_torpig.write(Combo + '\n')
					File_torpig.close()
				elif 'immo' in SET(Combo):
					File_immo = open('immo.txt', 'a')
					File_immo.write(Combo + '\n')
					File_immo.close()
				elif 'ppe' in SET(Combo):
					File_ppe = open('ppe.txt', 'a')
					File_ppe.write(Combo + '\n')
					File_ppe.close()
				elif 'rt' in SET(Combo):
					File_rt = open('rt.txt', 'a')
					File_rt.write(Combo + '\n')
					File_rt.close()
				elif 'server' in SET(Combo):
					File_server = open('server.txt', 'a')
					File_server.write(Combo + '\n')
					File_server.close()
				elif 'hosting' in SET(Combo):
					File_hosting = open('hosting.txt', 'a')
					File_hosting.write(Combo + '\n')
					File_hosting.close()
				elif 'swiss' in SET(Combo):
					File_swiss = open('swiss.txt', 'a')
					File_swiss.write(Combo + '\n')
					File_swiss.close()
				elif 'absys' in SET(Combo):
					File_absys = open('absys.txt', 'a')
					File_absys.write(Combo + '\n')
					File_absys.close()
				elif 'cfi' in SET(Combo):
					File_cfi = open('cfi.txt', 'a')
					File_cfi.write(Combo + '\n')
					File_cfi.close()
				elif 'network' in SET(Combo):
					File_network = open('network.txt', 'a')
					File_network.write(Combo + '\n')
					File_network.close()
				elif 'ags' in SET(Combo):
					File_ags = open('ags.txt', 'a')
					File_ags.write(Combo + '\n')
					File_ags.close()
		except:
			pass

if __name__ == '__main__':
	List = open(sys.argv[1], 'r').read().splitlines()
	POOL = ThreadPool(200)
	POOL.map(Run, List)
	POOL.close()
	POOL.join()
	raw_input("BETO")