//  Written by hand on 2026-11-25 from
//  QtNfc/6.12.0/QtNfc/private/neard_helper_p.h, Qt 6.12.0, from Qt's
//  source (the Linux kit of Qt is built without neard and does not
//  have the header; Qt installs it as given here where it is built
//  with the feature 'neard'). Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object ('metaObject'
//  included).
//  Not written: the constructor, 'tr', 'instance', 'dbusObjectManager'
//  (not inline), the signals and the private slots. The class declares
//  no destructor, so none is written.
#include <QtNfc/qtnfcglobal.h>
#include <QtNfc/qtnfc-config.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(neard)
#include <QtNfc/6.12.0/QtNfc/private/neard_helper_p.h>
#include <QtCore/qmetaobject.h>

//  const QMetaObject *NeardHelper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11NeardHelper10metaObjectEv(
    const NeardHelper *self) {
  return self->metaObject();
}

#endif  // QT_CONFIG(neard)
