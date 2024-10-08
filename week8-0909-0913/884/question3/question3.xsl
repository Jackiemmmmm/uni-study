<?xml version="1.0"?>
<xsl:stylesheet
  version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns="http://www.w3.org/1999/xhtml">
  <xsl:output method="xml" indent="yes" encoding="UTF-8" />
  <xsl:template match="/audit">
    <html>
      <head>
        <title></title>
      </head>
      <body>
        <h1>Enrolment statistics</h1>
        <div>
          <strong>Campus: </strong>
          <xsl:value-of select="@campus" />
        </div>
        <div>
          <strong>Year: </strong>
          <xsl:value-of select="@year" />
        </div>
        <div>
          <strong>Session: </strong>
          <xsl:value-of select="@session" />
        </div>
        <br />
        <table border="1">
          <tr>
            <th>ID</th>
            <th>Subject</th>
            <th>Enrol</th>
            <th>Withdrawn</th>
          </tr>
          <xsl:for-each select="subject">
            <tr>
              <td>
                <xsl:value-of select="@sid" />
              </td>
              <td>
                <xsl:value-of select="code" />
                <xsl:text>: </xsl:text>
                <xsl:value-of select="title" />
              </td>
              <xsl:for-each select="statistics">
                <td>
                  <xsl:value-of select="enrol" />
                </td>
                <td>
                  <xsl:value-of select="withdrawn" />
                </td>
              </xsl:for-each>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>