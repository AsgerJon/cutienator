//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlayout_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qlayout.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QLayoutPrivate that Python can take functions over in. Every QLayoutPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLayoutPrivateCall0)(const void *, int, QLayoutItem *, int *);
class CuteQLayoutPrivate : public QLayoutPrivate {
public:
  using QLayoutPrivate::QLayoutPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QLayoutPrivate9replaceAtEiP11QLayoutItem")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QLayoutItem *QLayoutPrivate::replaceAt(int a0, QLayoutItem *a1)
  QLayoutItem *replaceAt(int a0, QLayoutItem *a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQLayoutPrivateCall0 call = reinterpret_cast<CuteQLayoutPrivateCall0>(taken[0]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QLayoutPrivate::replaceAt(a0, a1);
  }
};

//  QLayout *QLayoutPrivate::q_func()
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN14QLayoutPrivate6q_funcEv(QLayoutPrivate *self) {
  return self->q_func();
}

//  const QLayout *QLayoutPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QLayout *ritual_ZNK14QLayoutPrivate6q_funcEv(
    const QLayoutPrivate *self) {
  return self->q_func();
}

//  QLayoutPrivate::QLayoutPrivate()
extern "C" Q_DECL_EXPORT
QLayoutPrivate *ritual_ZN14QLayoutPrivateC1Ev() {
  return new CuteQLayoutPrivate();
}

//  void QLayoutPrivate::getMargin(int *result, int userMargin,
//      QStyle::PixelMetric pm) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QLayoutPrivate9getMarginEPiiN6QStyle11PixelMetricE(
    const QLayoutPrivate *self,
    int *result,
    int userMargin,
    QStyle::PixelMetric pm) {
  self->getMargin(result, userMargin, pm);
}

//  void QLayoutPrivate::doResize()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLayoutPrivate8doResizeEv(QLayoutPrivate *self) {
  self->doResize();
}

//  void QLayoutPrivate::reparentChildWidgets(QWidget *mw)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLayoutPrivate20reparentChildWidgetsEP7QWidget(
    QLayoutPrivate *self,
    QWidget *mw) {
  self->reparentChildWidgets(mw);
}

//  bool QLayoutPrivate::checkWidget(QWidget *widget) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QLayoutPrivate11checkWidgetEP7QWidget(
    const QLayoutPrivate *self,
    QWidget *widget) {
  return self->checkWidget(widget);
}

//  bool QLayoutPrivate::checkLayout(QLayout *otherLayout) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QLayoutPrivate11checkLayoutEP7QLayout(
    const QLayoutPrivate *self,
    QLayout *otherLayout) {
  return self->checkLayout(otherLayout);
}

//  QWidgetItem *QLayoutPrivate::createWidgetItem(const QLayout *layout,
//      QWidget *widget)
extern "C" Q_DECL_EXPORT
QWidgetItem *ritual_ZN14QLayoutPrivate16createWidgetItemEPK7QLayoutP7QWidget(
    const QLayout *layout,
    QWidget *widget) {
  return QLayoutPrivate::createWidgetItem(layout, widget);
}

//  QSpacerItem *QLayoutPrivate::createSpacerItem(const QLayout *layout, int
//      w, int h, QSizePolicy::Policy hPolicy, QSizePolicy::Policy vPolicy)
extern "C" Q_DECL_EXPORT
QSpacerItem *ritual_ZN14QLayoutPrivate16createSpacerItemEPK7QLayoutiiN11QSizePolicy6PolicyES4_(
    const QLayout *layout,
    int w,
    int h,
    QSizePolicy::Policy hPolicy,
    QSizePolicy::Policy vPolicy) {
  return QLayoutPrivate::createSpacerItem(layout, w, h, hPolicy, vPolicy);
}

//  QLayoutItem *QLayoutPrivate::replaceAt(int a0, QLayoutItem *a1)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN14QLayoutPrivate9replaceAtEiP11QLayoutItem(
    QLayoutPrivate *self,
    int a0,
    QLayoutItem *a1) {
  return self->replaceAt(a0, a1);
}

//  a Python function taken by a CuteQLayoutPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLayoutPrivate(
    QLayoutPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLayoutPrivate *>(self)->take(key, call);
}

//  QLayoutItem *QLayoutPrivate::replaceAt(int a0, QLayoutItem *a1)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZN14QLayoutPrivate9replaceAtEiP11QLayoutItem(
    QLayoutPrivate *self,
    int a0,
    QLayoutItem *a1) {
  return self->QLayoutPrivate::replaceAt(a0, a1);
}
