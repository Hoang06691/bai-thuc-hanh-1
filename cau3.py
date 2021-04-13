<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Administrator"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2021-03-02 05:10:11 PM"/>
        <attribute name="created" value="QWRtaW5pc3RyYXRvcjtBRE1JTjsyMDIxLTAzLTAyOzA0OjU5OjUzIFBNOzMwMTg="/>
        <attribute name="edited" value="QWRtaW5pc3RyYXRvcjtBRE1JTjsyMDIxLTAzLTAyOzA1OjEwOjExIFBNOzI7MzEwOQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="x" type="Integer" array="False" size=""/>
            <output expression="&quot;input the radius of the circle&quot;" newline="True"/>
            <input variable="x"/>
            <output expression="&quot;Area is&quot;&amp;Circle(x)" newline="True"/>
        </body>
    </function>
    <function name="Circle" type="Real" variable="Area">
        <parameters>
            <parameter name="Radius" type="Real" array="False"/>
        </parameters>
        <body>
            <declare name="Area" type="Real" array="False" size=""/>
            <assign variable="Area" expression="Pi*radius^2"/>
        </body>
    </function>
</flowgorithm>
