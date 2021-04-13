<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Administrator"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2021-03-02 05:15:50 PM"/>
        <attribute name="created" value="QWRtaW5pc3RyYXRvcjtBRE1JTjsyMDIxLTAzLTAyOzA1OjExOjAyIFBNOzMwMDE="/>
        <attribute name="edited" value="QWRtaW5pc3RyYXRvcjtBRE1JTjsyMDIxLTAzLTAyOzA1OjE1OjUwIFBNOzE7MzExNg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n" type="Integer" array="False" size=""/>
            <for variable="n" start="99" end="1" direction="dec" step="1">
                <if expression="n==1">
                    <then>
                        <output expression="&quot;one bottle of beer on the wall&quot;" newline="True"/>
                    </then>
                    <else>
                        <output expression="n&amp;&quot;bottles of beer on the wall&quot;" newline="True"/>
                    </else>
                </if>
            </for>
        </body>
    </function>
</flowgorithm>
