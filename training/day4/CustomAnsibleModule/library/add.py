from ansible.module_utils.basic import AnsibleModule

def add(a,b):
        return a + b

def main():
        module = AnsibleModule (
                    argument_spec=dict(
                      p=dict(type='float', required='yes'),
                      q=dict(type='float', required='yes')
                     )
                    )
        a= module.params['p']
        b= module.params['q']

        response = add ( a,b )

        #module.fail_json(msg='Fatal error occurred')
        module.exit_json(meta=response, changed=False)
main()
