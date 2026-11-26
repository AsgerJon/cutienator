//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>
#include <QtCore/QVector>

//  A QRhiShaderResourceBindings that Python can take functions over in. Every QRhiShaderResourceBindings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiShaderResourceBindingsCall0)(const void *, int *);
typedef bool (*CuteQRhiShaderResourceBindingsCall1)(const void *, int *);
typedef void (*CuteQRhiShaderResourceBindingsCall2)(const void *, int, int *);
typedef void (*CuteQRhiShaderResourceBindingsCall3)(const void *, int *);
class CuteQRhiShaderResourceBindings : public QRhiShaderResourceBindings {
public:
  using QRhiShaderResourceBindings::QRhiShaderResourceBindings;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QRhiShaderResourceBindings6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QRhiShaderResourceBindings15updateResourcesE6QFlagsINS_10UpdateFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiShaderResourceBindings::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiShaderResourceBindingsCall0 call = reinterpret_cast<CuteQRhiShaderResourceBindingsCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiShaderResourceBindings::resourceType();
  }

  //  bool QRhiShaderResourceBindings::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiShaderResourceBindingsCall1 call = reinterpret_cast<CuteQRhiShaderResourceBindingsCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QRhiShaderResourceBindings::updateResources(UpdateFlags flags)
  void updateResources(
      QRhiShaderResourceBindings::UpdateFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiShaderResourceBindingsCall2 call = reinterpret_cast<CuteQRhiShaderResourceBindingsCall2>(taken[2]);
      call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiShaderResourceBindingsCall3 call = reinterpret_cast<CuteQRhiShaderResourceBindingsCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiShaderResourceBindings::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK26QRhiShaderResourceBindings12resourceTypeEv(
    const QRhiShaderResourceBindings *self) {
  return self->resourceType();
}

//  void QRhiShaderResourceBindings::setBindings(std::initializer_list<QRhiSh
//      aderResourceBinding> list)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiShaderResourceBindings11setBindingsESt16initializer_listI25QRhiShaderResourceBindingE(
    QRhiShaderResourceBindings *self,
    const std::initializer_list<QRhiShaderResourceBinding> *list) {
  self->setBindings(*list);
}

//  const QRhiShaderResourceBinding
//      *QRhiShaderResourceBindings::cbeginBindings() const
extern "C" Q_DECL_EXPORT
const QRhiShaderResourceBinding *ritual_ZNK26QRhiShaderResourceBindings14cbeginBindingsEv(
    const QRhiShaderResourceBindings *self) {
  return self->cbeginBindings();
}

//  const QRhiShaderResourceBinding
//      *QRhiShaderResourceBindings::cendBindings() const
extern "C" Q_DECL_EXPORT
const QRhiShaderResourceBinding *ritual_ZNK26QRhiShaderResourceBindings12cendBindingsEv(
    const QRhiShaderResourceBindings *self) {
  return self->cendBindings();
}

//  const QRhiShaderResourceBinding
//      *QRhiShaderResourceBindings::bindingAt(qsizetype index) const
extern "C" Q_DECL_EXPORT
const QRhiShaderResourceBinding *ritual_ZNK26QRhiShaderResourceBindings9bindingAtEx(
    const QRhiShaderResourceBindings *self,
    qsizetype index) {
  return self->bindingAt(index);
}

//  qsizetype QRhiShaderResourceBindings::bindingCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK26QRhiShaderResourceBindings12bindingCountEv(
    const QRhiShaderResourceBindings *self) {
  return self->bindingCount();
}

//  bool QRhiShaderResourceBindings::isLayoutCompatible(const
//      QRhiShaderResourceBindings *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QRhiShaderResourceBindings18isLayoutCompatibleEPKS_(
    const QRhiShaderResourceBindings *self,
    const QRhiShaderResourceBindings *other) {
  return self->isLayoutCompatible(other);
}

//  QVector<quint32>
//      QRhiShaderResourceBindings::serializedLayoutDescription() const
extern "C" Q_DECL_EXPORT
QVector<quint32> *ritual_ZNK26QRhiShaderResourceBindings27serializedLayoutDescriptionEv(
    const QRhiShaderResourceBindings *self) {
  return new QVector<quint32>(self->serializedLayoutDescription());
}

//  bool QRhiShaderResourceBindings::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QRhiShaderResourceBindings6createEv(
    QRhiShaderResourceBindings *self) {
  return self->create();
}

//  void QRhiShaderResourceBindings::updateResources(UpdateFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiShaderResourceBindings15updateResourcesE6QFlagsINS_10UpdateFlagEE(
    QRhiShaderResourceBindings *self,
    int flags) {
  self->updateResources(
      QFlags<QRhiShaderResourceBindings::UpdateFlag>::fromInt(flags));
}

//  QRhiShaderResourceBindings::QRhiShaderResourceBindings(QRhiImplementation
//      *rhi)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZN26QRhiShaderResourceBindingsC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQRhiShaderResourceBindings(rhi);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QRhiShaderResourceBindings &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK26QRhiShaderResourceBindings(
    const QDebug *a0,
    const QRhiShaderResourceBindings *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  a Python function taken by a CuteQRhiShaderResourceBindings, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiShaderResourceBindings(
    QRhiShaderResourceBindings *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiShaderResourceBindings *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiShaderResourceBindings::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK26QRhiShaderResourceBindings12resourceTypeEv(
    const QRhiShaderResourceBindings *self) {
  return self->QRhiShaderResourceBindings::resourceType();
}

//  a QVector<quint32> a ritual of QRhiShaderResourceBindings gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QRhiShaderResourceBindings__QVector_quint32(
    QVector<quint32> *self) {
  delete self;
}
