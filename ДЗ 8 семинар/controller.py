import input_data
import output_data
import logger


def activate():
    accept = 'да'
    while accept == 'да':
        opertion = input_data.user_choice()
        match opertion:
            case 1:
                logger.logger_add_puple()
                output_data.print_puple()
            case 2:
                logger.logger_add_class()
                output_data.print_class()
            case 3:
                output_data.print_puple()
            case 4:
                output_data.print_class()
            case 5:
                logger.find_data()
            case 6:
                logger.logger_del()

        accept = input('Вы хотите еще что-то сделать? Да/Нет: ').lower()
        print('Всего доброго.')

