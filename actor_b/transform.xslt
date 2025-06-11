<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/person">
    <user>
      <fullName>
        <xsl:value-of select="name"/>
      </fullName>
    </user>
  </xsl:template>
</xsl:stylesheet>
