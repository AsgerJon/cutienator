//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfont_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>

//  QFontPrivate::QFontPrivate()
extern "C" Q_DECL_EXPORT
QFontPrivate *ritual_ZN12QFontPrivateC1Ev() {
  return new QFontPrivate();
}

//  QFontPrivate::QFontPrivate(const QFontPrivate &other)
extern "C" Q_DECL_EXPORT
QFontPrivate *ritual_ZN12QFontPrivateC1ERKS_(const QFontPrivate *other) {
  return new QFontPrivate(*other);
}

//  QFontPrivate::~QFontPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFontPrivateD1Ev(QFontPrivate *self) {
  delete self;
}

//  QFontEngine *QFontPrivate::engineForScript(int script) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZNK12QFontPrivate15engineForScriptEi(
    const QFontPrivate *self,
    int script) {
  return self->engineForScript(script);
}

//  QFont QFontPrivate::smallCapsFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK12QFontPrivate13smallCapsFontEv(const QFontPrivate *self) {
  return new QFont(self->smallCapsFont());
}

//  QFontPrivate *QFontPrivate::smallCapsFontPrivate() const
extern "C" Q_DECL_EXPORT
QFontPrivate *ritual_ZNK12QFontPrivate20smallCapsFontPrivateEv(
    const QFontPrivate *self) {
  return self->smallCapsFontPrivate();
}

//  QFontPrivate *QFontPrivate::get(const QFont &font)
extern "C" Q_DECL_EXPORT
QFontPrivate *ritual_ZN12QFontPrivate3getERK5QFont(const QFont *font) {
  return QFontPrivate::get(*font);
}

//  void QFontPrivate::resolve(uint mask, const QFontPrivate *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFontPrivate7resolveEjPKS_(
    QFontPrivate *self,
    uint mask,
    const QFontPrivate *other) {
  self->resolve(mask, other);
}

//  void QFontPrivate::detachButKeepEngineData(QFont *font)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFontPrivate23detachButKeepEngineDataEP5QFont(QFont *font) {
  QFontPrivate::detachButKeepEngineData(font);
}

//  void QFontPrivate::setFeature(QFont::Tag tag, quint32 value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFontPrivate10setFeatureEN5QFont3TagEj(
    QFontPrivate *self,
    const QFont::Tag *tag,
    quint32 value) {
  self->setFeature(*tag, value);
}

//  void QFontPrivate::unsetFeature(QFont::Tag tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFontPrivate12unsetFeatureEN5QFont3TagE(
    QFontPrivate *self,
    const QFont::Tag *tag) {
  self->unsetFeature(*tag);
}

//  void QFontPrivate::setVariableAxis(QFont::Tag tag, float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFontPrivate15setVariableAxisEN5QFont3TagEf(
    QFontPrivate *self,
    const QFont::Tag *tag,
    float value) {
  self->setVariableAxis(*tag, value);
}

//  void QFontPrivate::unsetVariableAxis(QFont::Tag tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFontPrivate17unsetVariableAxisEN5QFont3TagE(
    QFontPrivate *self,
    const QFont::Tag *tag) {
  self->unsetVariableAxis(*tag);
}

//  bool QFontPrivate::hasVariableAxis(QFont::Tag tag, float value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QFontPrivate15hasVariableAxisEN5QFont3TagEf(
    const QFontPrivate *self,
    const QFont::Tag *tag,
    float value) {
  return self->hasVariableAxis(*tag, value);
}
