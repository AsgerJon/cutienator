//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if !defined(QT_NO_QOBJECT)
#include <QtCore/qobject.h>

//  QObjectData::~QObjectData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QObjectDataD1Ev(QObjectData *self) {
  delete self;
}

#if !(QT_CORE_REMOVED_SINCE(6, 9) && defined(Q_COMPILER_MANGLES_RETURN_TYPE))
//  const QMetaObject *QObjectData::dynamicMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QObjectData17dynamicMetaObjectEv(
    const QObjectData *self) {
  return self->dynamicMetaObject();
}
#endif

#endif  // !defined(QT_NO_QOBJECT)
