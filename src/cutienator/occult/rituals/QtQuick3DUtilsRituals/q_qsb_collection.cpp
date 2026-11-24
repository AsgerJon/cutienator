//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QQsbCollection that Python can take functions over in. Every QQsbCollection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QQsbCollection::Entry * (*CuteQQsbCollectionCall0)(const void *, const QByteArray *, const QQsbCollection::EntryDesc *, int *);
class CuteQQsbCollection : public QQsbCollection {
public:
  using QQsbCollection::QQsbCollection;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQsbCollection8addEntryERK10QByteArrayRKNS_9EntryDescE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  Entry QQsbCollection::addEntry(const QByteArray &key, const EntryDesc
  //      &entryDesc)
  QQsbCollection::Entry addEntry(
      const QByteArray &key,
      const QQsbCollection::EntryDesc &entryDesc) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQsbCollectionCall0 call = reinterpret_cast<CuteQQsbCollectionCall0>(taken[0]);
      const QQsbCollection::Entry * given = call(this, &key, &entryDesc, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QQsbCollection::~QQsbCollection()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQsbCollectionD1Ev(QQsbCollection *self) {
  delete self;
}

//  Entry QQsbCollection::addEntry(const QByteArray &key, const EntryDesc
//      &entryDesc)
extern "C" Q_DECL_EXPORT
QQsbCollection::Entry *ritual_ZN14QQsbCollection8addEntryERK10QByteArrayRKNS_9EntryDescE(
    QQsbCollection *self,
    const QByteArray *key,
    const QQsbCollection::EntryDesc *entryDesc) {
  return new QQsbCollection::Entry(self->addEntry(*key, *entryDesc));
}

//  a Python function taken by a CuteQQsbCollection, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQsbCollection(
    QQsbCollection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQsbCollection *>(self)->take(key, call);
}
