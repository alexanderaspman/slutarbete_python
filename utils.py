def get_valid_input(prompt, input_type, validation_func, error_message="Ogiltigt värde. Försök igen."):
    while True:
        try:
            user_input = input_type(input(prompt))
            if validation_func(user_input):
                return user_input
            else:
               print(error_message)
        except ValueError:
            print(error_message)