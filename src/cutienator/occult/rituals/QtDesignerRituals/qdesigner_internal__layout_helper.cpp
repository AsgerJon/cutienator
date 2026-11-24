//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>

//  A qdesigner_internal::LayoutHelper that Python can take functions over in. Every qdesigner_internal::LayoutHelper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRect * (*Cuteqdesigner_internal_LayoutHelperCall0)(const void *, QLayout *, int, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall1)(const void *, QLayout *, const QRect *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall2)(const void *, QLayout *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall3)(const void *, QLayout *, QWidget *, QWidget *, int *);
typedef bool (*Cuteqdesigner_internal_LayoutHelperCall4)(const void *, const QDesignerFormEditorInterface *, const QWidget *, const QRect *, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall5)(const void *, const QDesignerFormEditorInterface *, QWidget *, const QRect *, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall6)(const void *, const QDesignerFormEditorInterface *, const QWidget *, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall7)(const void *, const QDesignerFormEditorInterface *, QWidget *, int *);
class Cuteqdesigner_internal_LayoutHelper : public qdesigner_internal::LayoutHelper {
public:
  using qdesigner_internal::LayoutHelper::LayoutHelper;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18qdesigner_internal12LayoutHelper8itemInfoEP7QLayouti")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper12insertWidgetEP7QLayoutRK5QRectP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper12removeWidgetEP7QLayoutP7QWidget")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper13replaceWidgetEP7QLayoutP7QWidgetS4_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18qdesigner_internal12LayoutHelper11canSimplifyEPK28QDesignerFormEditorInterfacePK7QWidgetRK5QRect")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper8simplifyEPK28QDesignerFormEditorInterfaceP7QWidgetRK5QRect")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper9pushStateEPK28QDesignerFormEditorInterfacePK7QWidget")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper8popStateEPK28QDesignerFormEditorInterfaceP7QWidget")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  QRect qdesigner_internal::LayoutHelper::itemInfo(QLayout *lt, int
  //      index) const
  QRect itemInfo(QLayout *lt, int index) const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall0 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall0>(taken[0]);
      const QRect * given = call(this, lt, index, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void qdesigner_internal::LayoutHelper::insertWidget(QLayout *lt,
  //      const QRect &info, QWidget *w)
  void insertWidget(QLayout *lt, const QRect &info, QWidget *w) override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall1 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall1>(taken[1]);
      call(this, lt, &info, w, &handled);
      if (handled) return;
    }
  }

  //  void qdesigner_internal::LayoutHelper::removeWidget(QLayout *lt,
  //      QWidget *widget)
  void removeWidget(QLayout *lt, QWidget *widget) override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall2 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall2>(taken[2]);
      call(this, lt, widget, &handled);
      if (handled) return;
    }
  }

  //  void qdesigner_internal::LayoutHelper::replaceWidget(QLayout *lt,
  //      QWidget *before, QWidget *after)
  void replaceWidget(QLayout *lt, QWidget *before, QWidget *after) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall3 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall3>(taken[3]);
      call(this, lt, before, after, &handled);
      if (handled) return;
    }
  }

  //  bool qdesigner_internal::LayoutHelper::canSimplify(const
  //      QDesignerFormEditorInterface *core, const QWidget
  //      *widgetWithManagedLayout, const QRect &restrictionArea) const
  bool canSimplify(
      const QDesignerFormEditorInterface *core,
      const QWidget *widgetWithManagedLayout,
      const QRect &restrictionArea) const override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall4 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall4>(taken[4]);
      bool given = call(this, core, widgetWithManagedLayout, &restrictionArea, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void qdesigner_internal::LayoutHelper::simplify(const
  //      QDesignerFormEditorInterface *core, QWidget
  //      *widgetWithManagedLayout, const QRect &restrictionArea)
  void simplify(
      const QDesignerFormEditorInterface *core,
      QWidget *widgetWithManagedLayout,
      const QRect &restrictionArea) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall5 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall5>(taken[5]);
      call(this, core, widgetWithManagedLayout, &restrictionArea, &handled);
      if (handled) return;
    }
  }

  //  void qdesigner_internal::LayoutHelper::pushState(const
  //      QDesignerFormEditorInterface *core, const QWidget
  //      *widgetWithManagedLayout)
  void pushState(
      const QDesignerFormEditorInterface *core,
      const QWidget *widgetWithManagedLayout) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall6 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall6>(taken[6]);
      call(this, core, widgetWithManagedLayout, &handled);
      if (handled) return;
    }
  }

  //  void qdesigner_internal::LayoutHelper::popState(const
  //      QDesignerFormEditorInterface *core, QWidget
  //      *widgetWithManagedLayout)
  void popState(
      const QDesignerFormEditorInterface *core,
      QWidget *widgetWithManagedLayout) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall7 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall7>(taken[7]);
      call(this, core, widgetWithManagedLayout, &handled);
      if (handled) return;
    }
  }
};

//  qdesigner_internal::LayoutHelper::~LayoutHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelperD1Ev(
    qdesigner_internal::LayoutHelper *self) {
  delete self;
}

//  QRect qdesigner_internal::LayoutHelper::itemInfo(QLayout *lt, int index)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18qdesigner_internal12LayoutHelper8itemInfoEP7QLayouti(
    const qdesigner_internal::LayoutHelper *self,
    QLayout *lt,
    int index) {
  return new QRect(self->itemInfo(lt, index));
}

//  void qdesigner_internal::LayoutHelper::insertWidget(QLayout *lt, const
//      QRect &info, QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper12insertWidgetEP7QLayoutRK5QRectP7QWidget(
    qdesigner_internal::LayoutHelper *self,
    QLayout *lt,
    const QRect *info,
    QWidget *w) {
  self->insertWidget(lt, *info, w);
}

//  void qdesigner_internal::LayoutHelper::removeWidget(QLayout *lt, QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper12removeWidgetEP7QLayoutP7QWidget(
    qdesigner_internal::LayoutHelper *self,
    QLayout *lt,
    QWidget *widget) {
  self->removeWidget(lt, widget);
}

//  void qdesigner_internal::LayoutHelper::replaceWidget(QLayout *lt, QWidget
//      *before, QWidget *after)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper13replaceWidgetEP7QLayoutP7QWidgetS4_(
    qdesigner_internal::LayoutHelper *self,
    QLayout *lt,
    QWidget *before,
    QWidget *after) {
  self->replaceWidget(lt, before, after);
}

//  bool qdesigner_internal::LayoutHelper::canSimplify(const
//      QDesignerFormEditorInterface *core, const QWidget
//      *widgetWithManagedLayout, const QRect &restrictionArea) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal12LayoutHelper11canSimplifyEPK28QDesignerFormEditorInterfacePK7QWidgetRK5QRect(
    const qdesigner_internal::LayoutHelper *self,
    const QDesignerFormEditorInterface *core,
    const QWidget *widgetWithManagedLayout,
    const QRect *restrictionArea) {
  return self->canSimplify(core, widgetWithManagedLayout, *restrictionArea);
}

//  void qdesigner_internal::LayoutHelper::simplify(const
//      QDesignerFormEditorInterface *core, QWidget *widgetWithManagedLayout,
//      const QRect &restrictionArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper8simplifyEPK28QDesignerFormEditorInterfaceP7QWidgetRK5QRect(
    qdesigner_internal::LayoutHelper *self,
    const QDesignerFormEditorInterface *core,
    QWidget *widgetWithManagedLayout,
    const QRect *restrictionArea) {
  self->simplify(core, widgetWithManagedLayout, *restrictionArea);
}

//  void qdesigner_internal::LayoutHelper::pushState(const
//      QDesignerFormEditorInterface *core, const QWidget
//      *widgetWithManagedLayout)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper9pushStateEPK28QDesignerFormEditorInterfacePK7QWidget(
    qdesigner_internal::LayoutHelper *self,
    const QDesignerFormEditorInterface *core,
    const QWidget *widgetWithManagedLayout) {
  self->pushState(core, widgetWithManagedLayout);
}

//  void qdesigner_internal::LayoutHelper::popState(const
//      QDesignerFormEditorInterface *core, QWidget *widgetWithManagedLayout)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper8popStateEPK28QDesignerFormEditorInterfaceP7QWidget(
    qdesigner_internal::LayoutHelper *self,
    const QDesignerFormEditorInterface *core,
    QWidget *widgetWithManagedLayout) {
  self->popState(core, widgetWithManagedLayout);
}

//  a Python function taken by a Cuteqdesigner_internal_LayoutHelper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_LayoutHelper(
    qdesigner_internal::LayoutHelper *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_LayoutHelper *>(self)->take(key, call);
}
