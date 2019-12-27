I'm using Python 3.8.1 for this. The date is 12/26/2019. My name is Jared Kelnhofer. Now let's get into the fun stuff!

The basic idea for this project is a neural network. I'm trying to do a bit of reinventing the wheel, so that I
get the opportunity to learn a bit about neural networks, and see if I can come up with anything useful. This project
is going to be geared towards simple LINEAR functions to start out with. Right now, I know literally next to nothing
about neural nets, but I've seen a few pictures, and have concocted my own idea of how to do it. It's absurdly inefficient,
laughably slow, and totally awesome. When it's done, it should be able to:

    1) Take any linear function, and generate a giant data set out of it. The data set will consist of a specified number
       of X/Y coordinates, generated based on specified rules. (Amount of coordinates wanted, function domain)

    2) Generate a neural network based on given parameters. (Number of nodes, range of M and B in the linear function.)

    2) Use the created neural network to analyse a data set and attempt to reconstruct the function that created
       it in the first place.

In-Depth-Stuff:

        Data Sets:

            The data set is stored in a .txt file. Each point in the data set is on its own line. The X coordinate is stored
            between the "<" and ">" symbols, while the Y coordinate is stored between the "[" and "]" symbols. For example,
            if you generated a data set with the following parameters:

                Function: Y=2X+4
                Function_Domain(2, 9)
                Amount_Of_Coordinates(4)

            Your .txt file would look like this:

                <2>[8]
                <4>[12]
                <6>[16]
                <8>[20]

            Of course, you would likely have many more data points than 4, but this is just an example. The reason that the
            numbers 2, 4, 6, and 8 are chosen to be the X coordinates is simple. To find the numbers to use for X, simply take
            the domain of the function, and find as many averages as there are points desired. (I know that sounds complicated,
            so I'll explain it a different way.) If you have a domain that is 100 whole numbers long, and you want 10 different
            data points, your task is now to find 10 MEANS of your domain. That is to say, you want to have 10 numbers selected
            from your domain, that are equally spaced across the whole thing. You're slicing it up into pieces. Here's how you
            actually do that:

                1) Take the endpoints of your range of numbers. Now find the difference between them.
                2) Divide the resulting number by the number of means you want.
                3) Now we enter a loop. Start at the beginning number in the range. Now add the number you fond in step 2 to
                   that. The result is the second number in your list. (The first one was the starting number.) Keep doing this
                   until you are done!

        Neural Networks:

            A neural network is created based on certain parameters, (How many nodes, and the ranges of M and B in
            the linear functions of each Node.) If you


                Node:

                    A Node is a "step" in our process. If you have 500 Nodes, than 500 functions will be run against your
                    X values. Only the Nodes with the highest weights get kept and averaged, unless one Node has a track
                    record that is very good.The Structure of a Node is as follows:

                        Node{
                            Function -----------The function that the Node contains, and will run X through.
                            ChildNodes ---------The Branches connecting us to Nodes following our Node.
                            ParentNodes --------The Branches connecting us to Nodes preceding our Node.
                            }

                Branch:

                    A branch is a connection from one Node to another. A Branch is WEIGHTED, which means it contains a
                    number describing how important it is to use. A branch with a higher weight is more likely to be
                    used than a branch with a lower weight. The structure of a Branch is as follows:

                        Branch{
                            Weight---------------Every time this Node gets a result within accuracy E, add 1 to the weight.
                            Destination----------The Node that the Branch is pointing to.
                            Origin---------------The Node that has this Branch branching off it to another Node.
                            }

                Storage:

                        A neural network gets stored in a pair of .txt files inside it's own directory, and so does it's
                        fine-tuned trained version. The file structure of the neural network and trained network look like
                        this:

                            neural_network/
                                branches.txt
                                nodes.txt

                            trained_network/
                                branches.txt
                                nodes.txt

                        The structure of the .txt files will remain the same between both network models. The only major
                        change from the actual code to the storage of the components is the addition of ID's. Each Node
                        has an ID when in a .txt file, and so does each Branch. This is so that they can reference each
                        other during the long-term.

                            Node structure:

                                There is one Node per line in the document. A Node starts with a "<" symbol and ends
                                with a ">" symbol. The ID starts after a "{" symbol and ends before the "}" symbol.
                                The function of the node starts after the "[" symbol and ends before the "]" symbol. The
                                list of child node branches starts after the "@" symbol and ends before the "%" symbol.
                                The list of parent node branches starts after the "^" symbol and ends before the "&" symbol.

                                To recap:

                                    <>-----Node container
                                    {}-----ID container
                                    []-----Function container
                                    @%-----Child Node Branch container
                                    ^&-----Parent Node Branch container

                                Example Node .txt file:

                                    <{0}[Y=2X+4]@4,%^4,5,7,2&>
                                    <{1}[Y=5X+6]@4,5,6,7%^4,4,6,8&>
                                    <{2}[Y=6X-4]@3,5,6,8%^5,6,7,8&>
                                    <{3}[Y=44X-6]@4,3,7,8%^4,5,6,7&>
                                    <{4}[Y=X+4]@1,5,7,8%^3,4,6,7&>

                            Branch structure:

                                There is one Branch per line in the document. A Branch starts with the "<" symbol and
                                ends with the ">" symbol. The Branch ID starts with a "{" and ends with a "}", and the
                                weight starts with a "[" and ends with a "]", and the destination starts with a "@" and
                                ends with a "%", and the origin starts with a "^" and ends with a "&".

                                To recap:

                                    <>-----Branch container
                                    {}-----ID container
                                    []-----Weight container
                                    @%-----Destination container
                                    ^&-----Origin container

Ok, that was a lot of planning. Let's write some code.