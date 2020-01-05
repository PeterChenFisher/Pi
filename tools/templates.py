key_success = 'success'
key_data = 'data'
key_message = 'message'
key_no_face = 'no_face'
key_not_recognized = 'not_recognized'
key_recognized = 'recognized'
key_illegal_face = 'illegal_face'


def template(success=False, data={}, message=''):
    """
    use success and data if success
    use message if failed
    :param success: default False
    :param data:
    :param message:
    :return:
    """
    return {
        key_success: success,
        key_data: data,
        key_message: message,
    }