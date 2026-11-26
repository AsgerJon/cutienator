//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/utils_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlocale.h>
#include <QtGui/qquaternion.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QPainter>
#include <QtGui/QOpenGLContext>
#include <QtGui/QOffscreenSurface>
#include <QtGui/qquaternion.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QRegularExpression>
#include <QtCore/QLocale>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 17, as local:utils.cpp:NUM_IN_POWER
#define NUM_IN_POWER(y, x) for (;y<x;y<<=1)

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 18, as local:utils.cpp:MIN_POWER
#define MIN_POWER 2

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 25, as _ZN5Utils20getNearestPowerOfTwoEj
inline GLuint Utils::getNearestPowerOfTwo(GLuint value)
{
    GLuint powOfTwoValue = MIN_POWER;
    NUM_IN_POWER(powOfTwoValue, value);
    return powOfTwoValue;
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 32, as _ZN5Utils15vectorFromColorERK6QColor
inline QVector4D Utils::vectorFromColor(const QColor &color)
{
    return QVector4D(color.redF(), color.greenF(), color.blueF(), color.alphaF());
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 37, as _ZN5Utils15colorFromVectorERK9QVector3D
inline QColor Utils::colorFromVector(const QVector3D &colorVector)
{
    return QColor(colorVector.x() * 255.0f, colorVector.y() * 255.0f,
                  colorVector.z() * 255.0f, 255.0f);
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 43, as _ZN5Utils15colorFromVectorERK9QVector4D
inline QColor Utils::colorFromVector(const QVector4D &colorVector)
{
    return QColor(colorVector.x() * 255.0f, colorVector.y() * 255.0f,
                  colorVector.z() * 255.0f, colorVector.w() * 255.0f);
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 172, as _ZN5Utils12getSelectionE6QPointi
inline QVector4D Utils::getSelection(QPoint mousepos, int height)
{
    // This is the only one that works with OpenGL ES 2.0, so we're forced to use it
    // Item count will be limited to 256*256*256
    GLubyte pixel[4] = {255, 255, 255, 255};
    QOpenGLContext::currentContext()->functions()->glReadPixels(mousepos.x(), height - mousepos.y(),
                                                                1, 1, GL_RGBA, GL_UNSIGNED_BYTE,
                                                                (void *)pixel);
    QVector4D selectedColor(pixel[0], pixel[1], pixel[2], pixel[3]);
    return selectedColor;
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 184, as _ZN5Utils16getGradientImageER15QLinearGradient
inline QImage Utils::getGradientImage(QLinearGradient &gradient)
{
    QImage image(QSize(gradientTextureWidth, gradientTextureHeight), QImage::Format_RGB32);
    gradient.setFinalStop(qreal(gradientTextureWidth), qreal(gradientTextureHeight));
    gradient.setStart(0.0, 0.0);

    QPainter pmp(&image);
    pmp.setBrush(QBrush(gradient));
    pmp.setPen(Qt::NoPen);
    pmp.drawRect(0, 0, int(gradientTextureWidth), int(gradientTextureHeight));
    return image;
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 197, as _ZN5Utils14preParseFormatERK7QStringRS0_S3_RiRc
inline Utils::ParamType Utils::preParseFormat(const QString &format, QString &preStr, QString &postStr,
                                       int &precision, char &formatSpec)
{
    static QRegularExpression formatMatcher(QStringLiteral("^([^%]*)%([\\-\\+#\\s\\d\\.lhjztL]*)([dicuoxfegXFEG])(.*)$"));
    static QRegularExpression precisionMatcher(QStringLiteral("\\.(\\d+)"));

    Utils::ParamType retVal;

    QRegularExpressionMatch formatMatch = formatMatcher.match(format, 0);

    if (formatMatch.hasMatch()) {
        preStr = formatMatch.captured(1);
        // Six and 'g' are defaults in Qt API
        precision = 6;
        if (!formatMatch.captured(2).isEmpty()) {
            QRegularExpressionMatch precisionMatch = precisionMatcher.match(formatMatch.captured(2),
                                                                            0);
            if (precisionMatch.hasMatch())
                precision = precisionMatch.captured(1).toInt();
        }
        if (formatMatch.captured(3).isEmpty())
            formatSpec = 'g';
        else
            formatSpec = formatMatch.captured(3).at(0).toLatin1();
        postStr = formatMatch.captured(4);
        retVal = mapFormatCharToParamType(formatSpec);
    } else {
        retVal = ParamTypeUnknown;
        // The out parameters are irrelevant in unknown case
    }

    return retVal;
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 248, as _ZN5Utils18formatLabelSprintfERK10QByteArrayNS_9ParamTypeEd
inline QString Utils::formatLabelSprintf(const QByteArray &format, Utils::ParamType paramType, qreal value)
{
    switch (paramType) {
    case ParamTypeInt:
        return QString::asprintf(format.constData(), qint64(value));
    case ParamTypeUInt:
        return QString::asprintf(format.constData(), quint64(value));
    case ParamTypeReal:
        return QString::asprintf(format.constData(), value);
    default:
        // Return format string to detect errors. Bars selection label logic also depends on this.
        return QString::fromUtf8(format);
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 263, as _ZN5Utils20formatLabelLocalizedENS_9ParamTypeEdRK7QLocaleRK7QStringS6_icRK10QByteArray
inline QString Utils::formatLabelLocalized(Utils::ParamType paramType, qreal value,
                                    const QLocale &locale, const QString &preStr, const QString &postStr,
                                    int precision, char formatSpec, const QByteArray &format)
{
    switch (paramType) {
    case ParamTypeInt:
    case ParamTypeUInt:
        return preStr + locale.toString(qint64(value)) + postStr;
    case ParamTypeReal:
        return preStr + locale.toString(value, formatSpec, precision) + postStr;
    default:
        // Return format string to detect errors. Bars selection label logic also depends on this.
        return QString::fromUtf8(format);
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 279, as _ZN5Utils18defaultLabelFormatEv
inline QString Utils::defaultLabelFormat()
{
    static const QString defaultFormat(QStringLiteral("%.2f"));
    return defaultFormat;
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 285, as _ZN5Utils9wrapValueEfff
inline float Utils::wrapValue(float value, float min, float max)
{
    if (value > max) {
        value = min + (value - max);

        // In case single wrap fails, jump to opposite end.
        if (value > max)
            value = min;
    }

    if (value < min) {
        value = max + (value - min);

        // In case single wrap fails, jump to opposite end.
        if (value < min)
            value = max;
    }

    return value;
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 306, as _ZN5Utils17calculateRotationERK9QVector3D
inline QQuaternion Utils::calculateRotation(const QVector3D &xyzRotations)
{
    QQuaternion rotQuatX = QQuaternion::fromAxisAndAngle(1.0f, 0.0f, 0.0f, xyzRotations.x());
    QQuaternion rotQuatY = QQuaternion::fromAxisAndAngle(0.0f, 1.0f, 0.0f, xyzRotations.y());
    QQuaternion rotQuatZ = QQuaternion::fromAxisAndAngle(0.0f, 0.0f, 1.0f, xyzRotations.z());
    QQuaternion totalRotation = rotQuatY * rotQuatZ * rotQuatX;
    return totalRotation;
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 231, as _ZN5Utils24mapFormatCharToParamTypeEc
inline Utils::ParamType Utils::mapFormatCharToParamType(char formatSpec)
{
    ParamType retVal = ParamTypeUnknown;
    if (formatSpec == 'd' || formatSpec == 'i' || formatSpec == 'c') {
        retVal = ParamTypeInt;
    } else if (formatSpec == 'u' || formatSpec == 'o'
               || formatSpec == 'x'|| formatSpec == 'X') {
        retVal = ParamTypeUInt;
    } else if (formatSpec == 'f' || formatSpec == 'F'
               || formatSpec == 'e' || formatSpec == 'E'
               || formatSpec == 'g' || formatSpec == 'G') {
        retVal = ParamTypeReal;
    }

    return retVal;
}
//  -----------------------------------------------------------------------

//  GLuint Utils::getNearestPowerOfTwo(GLuint value)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN5Utils20getNearestPowerOfTwoEj(GLuint value) {
  return Utils::getNearestPowerOfTwo(value);
}

//  QVector4D Utils::vectorFromColor(const QColor &color)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN5Utils15vectorFromColorERK6QColor(const QColor *color) {
  return new QVector4D(Utils::vectorFromColor(*color));
}

//  QColor Utils::colorFromVector(const QVector3D &colorVector)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN5Utils15colorFromVectorERK9QVector3D(
    const QVector3D *colorVector) {
  return new QColor(Utils::colorFromVector(*colorVector));
}

//  QColor Utils::colorFromVector(const QVector4D &colorVector)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN5Utils15colorFromVectorERK9QVector4D(
    const QVector4D *colorVector) {
  return new QColor(Utils::colorFromVector(*colorVector));
}

//  QVector4D Utils::getSelection(QPoint mousepos, int height)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN5Utils12getSelectionE6QPointi(
    const QPoint *mousepos,
    int height) {
  return new QVector4D(Utils::getSelection(*mousepos, height));
}

//  QImage Utils::getGradientImage(QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN5Utils16getGradientImageER15QLinearGradient(
    QLinearGradient *gradient) {
  return new QImage(Utils::getGradientImage(*gradient));
}

//  ParamType Utils::preParseFormat(const QString &format, QString &preStr,
//      QString &postStr, int &precision, char &formatSpec)
extern "C" Q_DECL_EXPORT
Utils::ParamType ritual_ZN5Utils14preParseFormatERK7QStringRS0_S3_RiRc(
    const QString *format,
    QString *preStr,
    QString *postStr,
    int *precision,
    char *formatSpec) {
  return Utils::preParseFormat(
      *format,
      *preStr,
      *postStr,
      *precision,
      *formatSpec);
}

//  QString Utils::formatLabelSprintf(const QByteArray &format, ParamType
//      paramType, qreal value)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5Utils18formatLabelSprintfERK10QByteArrayNS_9ParamTypeEd(
    const QByteArray *format,
    Utils::ParamType paramType,
    qreal value) {
  return new QString(Utils::formatLabelSprintf(*format, paramType, value));
}

//  QString Utils::formatLabelLocalized(ParamType paramType, qreal value,
//      const QLocale &locale, const QString &preStr, const QString &postStr,
//      int precision, char formatSpec, const QByteArray &format)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5Utils20formatLabelLocalizedENS_9ParamTypeEdRK7QLocaleRK7QStringS6_icRK10QByteArray(
    Utils::ParamType paramType,
    qreal value,
    const QLocale *locale,
    const QString *preStr,
    const QString *postStr,
    int precision,
    char formatSpec,
    const QByteArray *format) {
  return new QString(
      Utils::formatLabelLocalized(
          paramType,
          value,
          *locale,
          *preStr,
          *postStr,
          precision,
          formatSpec,
          *format));
}

//  QString Utils::defaultLabelFormat()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5Utils18defaultLabelFormatEv() {
  return new QString(Utils::defaultLabelFormat());
}

//  float Utils::wrapValue(float value, float min, float max)
extern "C" Q_DECL_EXPORT
float ritual_ZN5Utils9wrapValueEfff(float value, float min, float max) {
  return Utils::wrapValue(value, min, max);
}

//  QQuaternion Utils::calculateRotation(const QVector3D &xyzRotations)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN5Utils17calculateRotationERK9QVector3D(
    const QVector3D *xyzRotations) {
  return new QQuaternion(Utils::calculateRotation(*xyzRotations));
}

//  ParamType Utils::mapFormatCharToParamType(char formatSpec)
extern "C" Q_DECL_EXPORT
Utils::ParamType ritual_ZN5Utils24mapFormatCharToParamTypeEc(
    char formatSpec) {
  return Utils::mapFormatCharToParamType(formatSpec);
}

//  Utils::~Utils()
extern "C" Q_DECL_EXPORT
void ritual_ZN5UtilsD1Ev(Utils *self) {
  delete self;
}
