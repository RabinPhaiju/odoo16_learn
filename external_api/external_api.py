import xmlrpc.client
url = 'http://0.0.0.0'
db = 'odoo'
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db,username,password,{})
print("🚀 ~ file: external_api.py:10 ~ uid", uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# leads = models.execute_kw(db,uid,password,'crm.lead','search',[[]],{'offset':0,'limit':5})
# leads = models.execute_kw(db,uid,password,'crm.lead','read',[leads],{'fields':['id','name']})
# print('------',leads)

# search read
# partner_rec = models.execute_kw(db,uid,password,'res.partner','search_read',[[['is_company','=',True]]],{'fields':['id','name']})
# print('parter_rec',partner_rec)

# create record
# vals = {
#     'name':'new xmlrpc'
# }
# created_id = models.execute_kw(db,uid,password,'res.partner','create',[vals])
# print('---',created_id)

# write record
# updated_id = models.execute_kw(db,uid,password,'res.partner','write',[[13],{'phone':'3434'}]) # 13 is id
# print('---',updated_id)

# delete record
# deleted_id = models.execute_kw(db,uid,password,'res.partner','unlink',[[13]])
# print('---',deleted_id)