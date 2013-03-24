This is an example for working with legacy code that I use in teaching.

The code is the Python version of the example that Brett Schuchert has used in talks about working with legacy code.

* Watch him work with the C# version: <http://vimeo.com/34484105>
    * Get the code [here](https://github.com/alexbepple/CurrencyConversion-CSharp-MSTest).
* See "[A story about too much power](http://schuchert.wikispaces.com/JMockIt.AStoryAboutTooMuchPower)" for a written treatment of the Java version of this example.


# Git tags

* `alpha` The legacy code we start out with.
* `beta` Now we have an integration test and a unit test that uses a Python form of monkey patching: namespace overriding.
* `gamma` Class extracted.
* `delta` Class for currency symbols extracted.
* `epsilon` Extracted caching to decorator pattern.
    * While very OO, it’s not very Pythonic. What would be a better solution? Something with Python decorators?


# Credits

Thanks to Brett Schuchert for this prolific example – and for generally publishing everything on [his wiki](http://schuchert.wikispaces.com/) under the [Creative Commons Attribution-ShareAlike license](http://creativecommons.org/licenses/by-sa/2.5/).


# License

This material is published under the same [CC BY-SA 2.5](http://www.typemock.com/isolator-product-page) license as Brett’s talk.

