//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <optional>
#include <QtCore/QMetaProperty>

//  A QQuick3DPropertyChangedTracker that Python can take functions over in. Every QQuick3DPropertyChangedTracker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DPropertyChangedTrackerCall0)(const void *, const QMetaProperty *, int, int *);
class CuteQQuick3DPropertyChangedTracker : public QQuick3DPropertyChangedTracker {
public:
  using QQuick3DPropertyChangedTracker::QQuick3DPropertyChangedTracker;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN30QQuick3DPropertyChangedTracker24markTrackedPropertyDirtyE13QMetaPropertyNS_17DirtyPropertyHintE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQuick3DPropertyChangedTracker::markTrackedPropertyDirty(QMetaPr
  //      operty property, DirtyPropertyHint hint)
  void markTrackedPropertyDirty(
      QMetaProperty property,
      QQuick3DPropertyChangedTracker::DirtyPropertyHint hint) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DPropertyChangedTrackerCall0 call = reinterpret_cast<CuteQQuick3DPropertyChangedTrackerCall0>(taken[0]);
      call(this, &property, static_cast<int>(hint), &handled);
      if (handled) return;
    }
  }
};

//  QQuick3DPropertyChangedTracker::~QQuick3DPropertyChangedTracker()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DPropertyChangedTrackerD1Ev(
    QQuick3DPropertyChangedTracker *self) {
  delete self;
}

//  QList<UniformProperty>
//      QQuick3DPropertyChangedTracker::extractProperties()
extern "C" Q_DECL_EXPORT
QList<QQuick3DPropertyChangedTracker::UniformProperty> *ritual_ZN30QQuick3DPropertyChangedTracker17extractPropertiesEv(
    QQuick3DPropertyChangedTracker *self) {
  return new QList<QQuick3DPropertyChangedTracker::UniformProperty>(
      self->extractProperties());
}

//  void QQuick3DPropertyChangedTracker::addPropertyWatcher(QMetaProperty
//      property, DirtyPropertyHint hint, QQuick3DObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DPropertyChangedTracker18addPropertyWatcherE13QMetaPropertyNS_17DirtyPropertyHintEP14QQuick3DObject(
    QQuick3DPropertyChangedTracker *self,
    const QMetaProperty *property,
    QQuick3DPropertyChangedTracker::DirtyPropertyHint hint,
    QQuick3DObject *object) {
  self->addPropertyWatcher(*property, hint, object);
}

//  void
//      QQuick3DPropertyChangedTracker::markTrackedPropertyDirty(QMetaPropert
//      y property, DirtyPropertyHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuick3DPropertyChangedTracker24markTrackedPropertyDirtyE13QMetaPropertyNS_17DirtyPropertyHintE(
    QQuick3DPropertyChangedTracker *self,
    const QMetaProperty *property,
    QQuick3DPropertyChangedTracker::DirtyPropertyHint hint) {
  self->markTrackedPropertyDirty(*property, hint);
}

//  std::optional<UniformProperty>
//      QQuick3DPropertyChangedTracker::createOrUpdateTrackedProperty(const
//      QMetaProperty property, bool addWatchers)
extern "C" Q_DECL_EXPORT
std::optional<QQuick3DPropertyChangedTracker::UniformProperty> *ritual_ZN30QQuick3DPropertyChangedTracker29createOrUpdateTrackedPropertyE13QMetaPropertyb(
    QQuick3DPropertyChangedTracker *self,
    const QMetaProperty *property,
    bool addWatchers) {
  return new std::optional<QQuick3DPropertyChangedTracker::UniformProperty>(
      self->createOrUpdateTrackedProperty(
          *property,
          addWatchers));
}

//  a Python function taken by a CuteQQuick3DPropertyChangedTracker, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DPropertyChangedTracker(
    QQuick3DPropertyChangedTracker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DPropertyChangedTracker *>(self)->take(key, call);
}

//  a QList<QQuick3DPropertyChangedTracker::UniformProperty> a ritual of
//      QQuick3DPropertyChangedTracker gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DPropertyChangedTracker__QList_QQuick3DPropertyChangedTracker_UniformProperty(
    QList<QQuick3DPropertyChangedTracker::UniformProperty> *self) {
  delete self;
}

//  a std::optional<QQuick3DPropertyChangedTracker::UniformProperty> a ritual
//      of QQuick3DPropertyChangedTracker gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DPropertyChangedTracker__std_optional_QQuick3DPropertyChangedTracker_UniformProperty(
    std::optional<QQuick3DPropertyChangedTracker::UniformProperty> *self) {
  delete self;
}
