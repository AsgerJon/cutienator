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
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>
#include <QtGui/qquaternion.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "utils_p.h"
#include <QtGui/QPainter>
#include <QtGui/QOpenGLContext>
#include <QtGui/QOffscreenSurface>
#include <QtGui/qquaternion.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QRegularExpression>
#include <QLocale>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
