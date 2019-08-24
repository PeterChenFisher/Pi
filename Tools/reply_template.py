key_data = 'data'
key_success = 'success'
key_message = 'message'


def template(success=False, data=None, message=None):
    return {key_data: data, key_success: success, key_message: message}
