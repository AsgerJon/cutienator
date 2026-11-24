//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickscalegrid_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickscalegrid_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickscalegrid_p_p.h>
#include <QtQml/qqml.h>
#include <QtCore/qiodevice.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickscalegrid.cpp, line 63, as _ZN21QQuickGridScaledImageC1Ev
inline QQuickGridScaledImage::QQuickGridScaledImage()
: _l(-1), _r(-1), _t(-1), _b(-1),
  _h(QQuickBorderImage::Stretch), _v(QQuickBorderImage::Stretch)
{
}

//  from ../qtdeclarative/src/quick/items/qquickscalegrid.cpp, line 69, as _ZN21QQuickGridScaledImageC1ERKS_
inline QQuickGridScaledImage::QQuickGridScaledImage(const QQuickGridScaledImage &o)
: _l(o._l), _r(o._r), _t(o._t), _b(o._b), _h(o._h), _v(o._v), _pix(o._pix)
{
}

//  from ../qtdeclarative/src/quick/items/qquickscalegrid.cpp, line 86, as _ZN21QQuickGridScaledImageC1EP9QIODevice
inline QQuickGridScaledImage::QQuickGridScaledImage(QIODevice *data)
: _l(-1), _r(-1), _t(-1), _b(-1), _h(QQuickBorderImage::Stretch), _v(QQuickBorderImage::Stretch)
{
    int l = -1;
    int r = -1;
    int t = -1;
    int b = -1;
    QString imgFile;

    QByteArray raw;
    while (raw = data->readLine(), !raw.isEmpty()) {
        QString line = QString::fromUtf8(raw.trimmed());
        if (line.isEmpty() || line.startsWith(QLatin1Char('#')))
            continue;

        int colonId = line.indexOf(QLatin1Char(':'));
        if (colonId <= 0)
            return;

        const QStringView property = QStringView{line}.left(colonId).trimmed();
        QStringView value = QStringView{line}.mid(colonId + 1).trimmed();

        if (property == QLatin1String("border.left")) {
            l = value.toInt();
        } else if (property == QLatin1String("border.right")) {
            r = value.toInt();
        } else if (property == QLatin1String("border.top")) {
            t = value.toInt();
        } else if (property == QLatin1String("border.bottom")) {
            b = value.toInt();
        } else if (property == QLatin1String("source")) {
            if (value.startsWith(QLatin1Char('"')) && value.endsWith(QLatin1Char('"')))
                value = value.mid(1, value.size() - 2); // remove leading/trailing quotes.
            imgFile = value.toString();
        } else if (property == QLatin1String("horizontalTileRule") || property == QLatin1String("horizontalTileMode")) {
            _h = stringToRule(value);
        } else if (property == QLatin1String("verticalTileRule") || property == QLatin1String("verticalTileMode")) {
            _v = stringToRule(value);
        }
    }

    if (l < 0 || r < 0 || t < 0 || b < 0 || imgFile.isEmpty())
        return;

    _l = l; _r = r; _t = t; _b = b;
    _pix = imgFile;
}

//  from ../qtdeclarative/src/quick/items/qquickscalegrid.cpp, line 151, as _ZNK21QQuickGridScaledImage7isValidEv
inline bool QQuickGridScaledImage::isValid() const
{
    return _l >= 0;
}

//  from ../qtdeclarative/src/quick/items/qquickscalegrid.cpp, line 156, as _ZNK21QQuickGridScaledImage8gridLeftEv
inline int QQuickGridScaledImage::gridLeft() const
{
    return _l;
}

//  from ../qtdeclarative/src/quick/items/qquickscalegrid.cpp, line 161, as _ZNK21QQuickGridScaledImage9gridRightEv
inline int QQuickGridScaledImage::gridRight() const
{
    return _r;
}

//  from ../qtdeclarative/src/quick/items/qquickscalegrid.cpp, line 166, as _ZNK21QQuickGridScaledImage7gridTopEv
inline int QQuickGridScaledImage::gridTop() const
{
    return _t;
}

//  from ../qtdeclarative/src/quick/items/qquickscalegrid.cpp, line 171, as _ZNK21QQuickGridScaledImage10gridBottomEv
inline int QQuickGridScaledImage::gridBottom() const
{
    return _b;
}

//  from ../qtdeclarative/src/quick/items/qquickscalegrid.cpp, line 176, as _ZNK21QQuickGridScaledImage9pixmapUrlEv
inline QString QQuickGridScaledImage::pixmapUrl() const
{
    return _pix;
}

//  from ../qtdeclarative/src/quick/items/qquickscalegrid.cpp, line 134, as _ZN21QQuickGridScaledImage12stringToRuleE11QStringView
inline QQuickBorderImage::TileMode QQuickGridScaledImage::stringToRule(QStringView s)
{
    QStringView string = s;
    if (string.startsWith(QLatin1Char('"')) && string.endsWith(QLatin1Char('"')))
        string = string.mid(1, string.size() - 2); // remove leading/trailing quotes.

    if (string == QLatin1String("Stretch") || string == QLatin1String("BorderImage.Stretch"))
        return QQuickBorderImage::Stretch;
    if (string == QLatin1String("Repeat") || string == QLatin1String("BorderImage.Repeat"))
        return QQuickBorderImage::Repeat;
    if (string == QLatin1String("Round") || string == QLatin1String("BorderImage.Round"))
        return QQuickBorderImage::Round;

    qWarning("QQuickGridScaledImage: Invalid tile rule specified. Using Stretch.");
    return QQuickBorderImage::Stretch;
}
//  -----------------------------------------------------------------------

//  QQuickGridScaledImage::QQuickGridScaledImage()
extern "C" Q_DECL_EXPORT
QQuickGridScaledImage *ritual_ZN21QQuickGridScaledImageC1Ev() {
  return new QQuickGridScaledImage();
}

//  QQuickGridScaledImage::QQuickGridScaledImage(const QQuickGridScaledImage
//      &a0)
extern "C" Q_DECL_EXPORT
QQuickGridScaledImage *ritual_ZN21QQuickGridScaledImageC1ERKS_(
    const QQuickGridScaledImage *a0) {
  return new QQuickGridScaledImage(*a0);
}

//  QQuickGridScaledImage::QQuickGridScaledImage(QIODevice *a0)
extern "C" Q_DECL_EXPORT
QQuickGridScaledImage *ritual_ZN21QQuickGridScaledImageC1EP9QIODevice(
    QIODevice *a0) {
  return new QQuickGridScaledImage(a0);
}

//  bool QQuickGridScaledImage::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickGridScaledImage7isValidEv(
    const QQuickGridScaledImage *self) {
  return self->isValid();
}

//  int QQuickGridScaledImage::gridLeft() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickGridScaledImage8gridLeftEv(
    const QQuickGridScaledImage *self) {
  return self->gridLeft();
}

//  int QQuickGridScaledImage::gridRight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickGridScaledImage9gridRightEv(
    const QQuickGridScaledImage *self) {
  return self->gridRight();
}

//  int QQuickGridScaledImage::gridTop() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickGridScaledImage7gridTopEv(
    const QQuickGridScaledImage *self) {
  return self->gridTop();
}

//  int QQuickGridScaledImage::gridBottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickGridScaledImage10gridBottomEv(
    const QQuickGridScaledImage *self) {
  return self->gridBottom();
}

//  QQuickBorderImage::TileMode QQuickGridScaledImage::horizontalTileRule()
//      const
extern "C" Q_DECL_EXPORT
QQuickBorderImage::TileMode ritual_ZNK21QQuickGridScaledImage18horizontalTileRuleEv(
    const QQuickGridScaledImage *self) {
  return self->horizontalTileRule();
}

//  QQuickBorderImage::TileMode QQuickGridScaledImage::verticalTileRule()
//      const
extern "C" Q_DECL_EXPORT
QQuickBorderImage::TileMode ritual_ZNK21QQuickGridScaledImage16verticalTileRuleEv(
    const QQuickGridScaledImage *self) {
  return self->verticalTileRule();
}

//  QString QQuickGridScaledImage::pixmapUrl() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuickGridScaledImage9pixmapUrlEv(
    const QQuickGridScaledImage *self) {
  return new QString(self->pixmapUrl());
}

//  QQuickBorderImage::TileMode
//      QQuickGridScaledImage::stringToRule(QStringView a0)
extern "C" Q_DECL_EXPORT
QQuickBorderImage::TileMode ritual_ZN21QQuickGridScaledImage12stringToRuleE11QStringView(
    const QString *a0) {
  return QQuickGridScaledImage::stringToRule(QStringView(*a0));
}

//  QQuickGridScaledImage::~QQuickGridScaledImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickGridScaledImageD1Ev(QQuickGridScaledImage *self) {
  delete self;
}
