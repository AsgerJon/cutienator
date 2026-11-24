//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/actionprovider_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/actionprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QDesignerActionProviderExtension that Python can take functions over in. Every QDesignerActionProviderExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRect * (*CuteQDesignerActionProviderExtensionCall0)(const void *, QAction *, int *);
typedef void * (*CuteQDesignerActionProviderExtensionCall1)(const void *, const QPoint *, int *);
typedef void (*CuteQDesignerActionProviderExtensionCall2)(const void *, const QPoint *, int *);
class CuteQDesignerActionProviderExtension : public QDesignerActionProviderExtension {
public:
  using QDesignerActionProviderExtension::QDesignerActionProviderExtension;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK32QDesignerActionProviderExtension14actionGeometryEP7QAction")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerActionProviderExtension8actionAtERK6QPoint")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerActionProviderExtension15adjustIndicatorERK6QPoint")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QRect QDesignerActionProviderExtension::actionGeometry(QAction
  //      *action) const
  QRect actionGeometry(QAction *action) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerActionProviderExtensionCall0 call = reinterpret_cast<CuteQDesignerActionProviderExtensionCall0>(taken[0]);
      const QRect * given = call(this, action, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QAction *QDesignerActionProviderExtension::actionAt(const QPoint
  //      &pos) const
  QAction *actionAt(const QPoint &pos) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerActionProviderExtensionCall1 call = reinterpret_cast<CuteQDesignerActionProviderExtensionCall1>(taken[1]);
      void * given = call(this, &pos, &handled);
      if (handled) return static_cast<QAction *>(given);
    }
    return {};
  }

  //  void QDesignerActionProviderExtension::adjustIndicator(const QPoint
  //      &pos)
  void adjustIndicator(const QPoint &pos) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerActionProviderExtensionCall2 call = reinterpret_cast<CuteQDesignerActionProviderExtensionCall2>(taken[2]);
      call(this, &pos, &handled);
      if (handled) return;
    }
  }
};

//  QDesignerActionProviderExtension::~QDesignerActionProviderExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerActionProviderExtensionD1Ev(
    QDesignerActionProviderExtension *self) {
  delete self;
}

//  QRect QDesignerActionProviderExtension::actionGeometry(QAction *action)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK32QDesignerActionProviderExtension14actionGeometryEP7QAction(
    const QDesignerActionProviderExtension *self,
    QAction *action) {
  return new QRect(self->actionGeometry(action));
}

//  QAction *QDesignerActionProviderExtension::actionAt(const QPoint &pos)
//      const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK32QDesignerActionProviderExtension8actionAtERK6QPoint(
    const QDesignerActionProviderExtension *self,
    const QPoint *pos) {
  return self->actionAt(*pos);
}

//  void QDesignerActionProviderExtension::adjustIndicator(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerActionProviderExtension15adjustIndicatorERK6QPoint(
    QDesignerActionProviderExtension *self,
    const QPoint *pos) {
  self->adjustIndicator(*pos);
}

//  a Python function taken by a CuteQDesignerActionProviderExtension, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerActionProviderExtension(
    QDesignerActionProviderExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerActionProviderExtension *>(self)->take(key, call);
}
