def main():

    ##################################################
    ##################################################

    m_perc = int(input("Enter number of males in class: "))
    f_perc = int(input("Enter number of females in class: "))


    print("\nThe total number of students:\t\t", m_perc + f_perc)
    print("The number of males and females\t\t", m_perc, "  ", f_perc)
    temp = m_perc
    m_perc = (m_perc/(m_perc + f_perc))*100
    f_perc = (f_perc/(temp + f_perc))*100
    print(f"The percentage of males and females\t {m_perc:.2f} {f_perc:.2f}")


    ########################################
    # Do not delete the return statement
    ########################################



    return m_perc, f_perc


if __name__ == '__main__':
    main()
