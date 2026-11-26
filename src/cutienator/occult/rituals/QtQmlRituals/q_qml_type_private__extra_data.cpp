//  Written by hand on 2026-11-25 from
//  QtQml/6.12.0/QtQml/private/qqmltype_p_p.h, Qt 6.12.0, from Qt's
//  source. Kept as it is when the generator runs again.
//  Qt does not export this union: only its destructor is written, which
//  is inline. Not written: the constructor, which is inline as well but
//  of a union Qt builds in place ('QQmlTypePrivate() does the actual
//  construction'). The union has the name of the member that holds it,
//  'extraData', so the compiler refused the generated file for the
//  name: it is written in full, as 'union QQmlTypePrivate::extraData'.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p_p.h>

//  QQmlTypePrivate::extraData::~extraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlTypePrivate9extraDataD1Ev(
    union QQmlTypePrivate::extraData *self) {
  delete self;
}
