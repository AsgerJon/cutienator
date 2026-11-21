//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextobject.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QTextBlockGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QTextBlockGroup10metaObjectEv(
    const QTextBlockGroup *self) {
  return self->metaObject();
}

//  QString QTextBlockGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QTextBlockGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextBlockGroup::tr(s, c, n));
}
