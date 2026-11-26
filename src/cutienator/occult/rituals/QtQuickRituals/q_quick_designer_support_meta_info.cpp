//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdesignersupportmetainfo_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_designer)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdesignersupportmetainfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  bool QQuickDesignerSupportMetaInfo::isSubclassOf(QObject *object, const
//      QByteArray &superTypeName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QQuickDesignerSupportMetaInfo12isSubclassOfEP7QObjectRK10QByteArray(
    QObject *object,
    const QByteArray *superTypeName) {
  return QQuickDesignerSupportMetaInfo::isSubclassOf(object, *superTypeName);
}

//  void
//      QQuickDesignerSupportMetaInfo::registerNotifyPropertyChangeCallBack(v
//      oid (*)(QObject *, const QQuickDesignerSupport::PropertyName &)
//      callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickDesignerSupportMetaInfo36registerNotifyPropertyChangeCallBackEPFvP7QObjectRK10QByteArrayE(
    void *callback) {
  QQuickDesignerSupportMetaInfo::registerNotifyPropertyChangeCallBack(
      reinterpret_cast<void (*)(QObject *, const QQuickDesignerSupport::PropertyName &)>(callback));
}

//  void QQuickDesignerSupportMetaInfo::registerMockupObject(const char *uri,
//      int versionMajor, int versionMinor, const char *qmlName)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickDesignerSupportMetaInfo20registerMockupObjectEPKciiS1_(
    const char *uri,
    int versionMajor,
    int versionMinor,
    const char *qmlName) {
  QQuickDesignerSupportMetaInfo::registerMockupObject(
      uri,
      versionMajor,
      versionMinor,
      qmlName);
}

//  QQuickDesignerSupportMetaInfo::~QQuickDesignerSupportMetaInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickDesignerSupportMetaInfoD1Ev(
    QQuickDesignerSupportMetaInfo *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_designer)
