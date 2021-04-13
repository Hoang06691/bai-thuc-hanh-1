<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Administrator"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2021-03-02 04:49:36 PM"/>
        <attribute name="created" value="QWRtaW5pc3RyYXRvcjtBRE1JTjsyMDIxLTAzLTAyOzA0OjQ0OjI0IFBNOzMwMTA="/>
        <attribute name="edited" value="QWRtaW5pc3RyYXRvcjtBRE1JTjsyMDIxLTAzLTAyOzA0OjQ5OjM2IFBNOzE7MzEyNg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="s, a, h" type="Real" array="False" size=""/>
            <output expression="&quot;nh&#7853;p chi&#7873;u d&#224;i &#273;&#225;y a:&quot;" newline="True"/>
            <input variable="a"/>
            <output expression="&quot;nhap chi&#7873;u cao h:&quot;" newline="True"/>
            <input variable="h"/>
            <if expression="a&gt;0&amp;&amp;h&gt;0">
                <then>
                    <assign variable="s" expression="(a*h)/2"/>
                    <output expression="&quot;dien tich la&quot;&amp;s" newline="True"/>
                </then>
                <else>
                    <output expression="&quot;khong hop le&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>
