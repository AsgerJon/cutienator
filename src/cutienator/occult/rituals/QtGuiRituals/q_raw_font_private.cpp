//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrawfont_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_RAWFONT)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrawfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtGui/qrawfont.h>

//  QRawFontPrivate::QRawFontPrivate()
extern "C" Q_DECL_EXPORT
QRawFontPrivate *ritual_ZN15QRawFontPrivateC1Ev() {
  return new QRawFontPrivate();
}

//  QRawFontPrivate::QRawFontPrivate(const QRawFontPrivate &other)
extern "C" Q_DECL_EXPORT
QRawFontPrivate *ritual_ZN15QRawFontPrivateC1ERKS_(
    const QRawFontPrivate *other) {
  return new QRawFontPrivate(*other);
}

//  QRawFontPrivate::~QRawFontPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRawFontPrivateD1Ev(QRawFontPrivate *self) {
  delete self;
}

//  void QRawFontPrivate::cleanUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRawFontPrivate7cleanUpEv(QRawFontPrivate *self) {
  self->cleanUp();
}

//  bool QRawFontPrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QRawFontPrivate7isValidEv(const QRawFontPrivate *self) {
  return self->isValid();
}

//  void QRawFontPrivate::setFontEngine(QFontEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRawFontPrivate13setFontEngineEP11QFontEngine(
    QRawFontPrivate *self,
    QFontEngine *engine) {
  self->setFontEngine(engine);
}

//  void QRawFontPrivate::loadFromData(const QByteArray &fontData, qreal
//      pixelSize, QFont::HintingPreference hintingPreference)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRawFontPrivate12loadFromDataERK10QByteArraydN5QFont17HintingPreferenceE(
    QRawFontPrivate *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  self->loadFromData(*fontData, pixelSize, hintingPreference);
}

//  QRawFontPrivate *QRawFontPrivate::get(const QRawFont &font)
extern "C" Q_DECL_EXPORT
QRawFontPrivate *ritual_ZN15QRawFontPrivate3getERK8QRawFont(
    const QRawFont *font) {
  return QRawFontPrivate::get(*font);
}

#endif  // !defined(QT_NO_RAWFONT)
