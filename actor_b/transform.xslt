<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:param name="q1"/>
  <xsl:param name="q2"/>
  <xsl:param name="q3"/>
  <xsl:param name="q4"/>
  <xsl:param name="q5"/>
  <xsl:param name="q6"/>

  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="/GoogleForm">
    <FormResponse>

      <Answer questionId="q1">
        <xsl:value-of select="$q1"/>
      </Answer>

      <Answer questionId="q2">
        <xsl:value-of select="$q2"/>
      </Answer>

      <xsl:if test="$q2 = 'Parțial'">
        <Answer questionId="q3">
          <xsl:value-of select="$q3"/>
        </Answer>
      </xsl:if>

      <Answer questionId="q4">
        <xsl:value-of select="$q4"/>
      </Answer>

      <Answer questionId="q5">
        <xsl:value-of select="$q5"/>
      </Answer>

      <xsl:if test="$q5 = 'Da'">
        <Answer questionId="q6">
          <xsl:value-of select="$q6"/>
        </Answer>
      </xsl:if>

    </FormResponse>
  </xsl:template>
</xsl:stylesheet>
