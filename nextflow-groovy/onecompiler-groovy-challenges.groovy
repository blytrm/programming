// 1 
println('Hello World')

// 2 : multi line print
println """
Hello
World
"""

// 3 : scan the name of the user + say hello
def name = System.in.newReader().readLine()
println "Hello " + name

// 4 : Take a character as an input and print whether it is an vowel or a consonant. Sample input and output are shown as below
def character = System.in.newReader().readLine()
def vowels = ['a', 'e', 'i', 'o', 'u']
if (vowels.contains(character)) {
    println "vowel"
} else {
    println "consonant"
}

// 5
