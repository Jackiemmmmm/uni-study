<?xml version="1.0"?>
<xsl:stylesheet
  version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns="http://www.w3.org/1999/xhtml">
  <xsl:output method="xml" indent="yes" encoding="UTF-8" />
  <xsl:template match="/result">
    <html>
      <head>
        <title></title>
        <style>
          table {
          border-spacing: 0.5rem;
          }
          td {
          border-style: dashed;
          padding: 0.5rem;
          }
          td:first-child {
          font-weight: bold;
          text-align: right;
          }
          td:last-child {
          color: red;
          font-size: 1.5rem;
          }
        </style>
      </head>
      <body>
        <h1>Exam result</h1>
        <table border="1">
          <tr>
            <td>Reference number: </td>
            <td>
              <xsl:value-of select="@ref" />
            </td>
          </tr>
          <tr>
            <td>Exam number: </td>
            <td>
              <xsl:value-of select="examId" />
            </td>
          </tr>
          <tr>
            <td>Constestant number: </td>
            <td>
              <xsl:value-of select="contestantId" />
            </td>
          </tr>
          <tr>
            <td>Digital signature: </td>
            <td>
              <xsl:value-of select="digitalSignature" />
            </td>
          </tr>
          <tr>
            <td>Score: </td>
            <td>
              <xsl:value-of select="score" />
            </td>
          </tr>
          <tr>
            <td>Band: </td>
            <td>
              <xsl:value-of select="band" />
            </td>
          </tr>

        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>