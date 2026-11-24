//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVarLengthGlyphLayoutArray::QVarLengthGlyphLayoutArray(int totalGlyphs)
extern "C" Q_DECL_EXPORT
QVarLengthGlyphLayoutArray *ritual_ZN26QVarLengthGlyphLayoutArrayC1Ei(
    int totalGlyphs) {
  return new QVarLengthGlyphLayoutArray(totalGlyphs);
}

//  void QVarLengthGlyphLayoutArray::resize(int totalGlyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QVarLengthGlyphLayoutArray6resizeEi(
    QVarLengthGlyphLayoutArray *self,
    int totalGlyphs) {
  self->resize(totalGlyphs);
}

//  QVarLengthGlyphLayoutArray::~QVarLengthGlyphLayoutArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QVarLengthGlyphLayoutArrayD1Ev(
    QVarLengthGlyphLayoutArray *self) {
  delete self;
}

//  QVarLengthGlyphLayoutArray as the QGlyphLayout it is built on
extern "C" Q_DECL_EXPORT
QGlyphLayout *ritual_cast_QVarLengthGlyphLayoutArray_QGlyphLayout(
    QVarLengthGlyphLayoutArray *self) {
  return static_cast<QGlyphLayout *>(self);
}
