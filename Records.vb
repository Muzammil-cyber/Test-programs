Module Module1
    Structure TcourseRec
        Dim Name As String
        Dim Marks As Integer
        Dim subjects As String

    End Structure
    Sub Main()
        Dim STD(5) As TcourseRec
        For x = 1 To 5
            Console.Write("Student's name: ")
            STD(x).Name = Console.ReadLine
            Console.Write("Subject selected: ")
            STD(x).subjects = Console.ReadLine
            Console.Write("Marks obtained: ")
            STD(x).Marks = Console.ReadLine
        Next
        For x = 1 To 5
            Console.Write(STD(x).Name)
            Console.Write(STD(x).subjects)
            Console.Write(STD(x).Marks)
        Next

        Console.ReadKey()

    End Sub

End Module
