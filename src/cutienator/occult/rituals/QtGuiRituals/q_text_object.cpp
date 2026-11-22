//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextobject.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextformat.h>

//  const QMetaObject *QTextObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QTextObject10metaObjectEv(
    const QTextObject *self) {
  return self->metaObject();
}

//  QString QTextObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTextObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextObject::tr(s, c, n));
}

//  QTextFormat QTextObject::format() const
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_ZNK11QTextObject6formatEv(const QTextObject *self) {
  return new QTextFormat(self->format());
}

//  int QTextObject::formatIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextObject11formatIndexEv(const QTextObject *self) {
  return self->formatIndex();
}

//  QTextDocument *QTextObject::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK11QTextObject8documentEv(const QTextObject *self) {
  return self->document();
}

//  int QTextObject::objectIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextObject11objectIndexEv(const QTextObject *self) {
  return self->objectIndex();
}
