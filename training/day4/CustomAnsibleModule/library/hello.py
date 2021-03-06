from ansible.module_utils.basic import AnsibleModule

def sayHello(message):
        return message

def main():
        module = AnsibleModule (
                    argument_spec=dict(
                      message=dict(type='str', required='yes')
                     )
                    )
        msg = module.params['message']

        response = sayHello(msg)

        module.fail_json(msg='Fatal error occurred')
        #module.exit_json(meta=response, changed=False)
main()
