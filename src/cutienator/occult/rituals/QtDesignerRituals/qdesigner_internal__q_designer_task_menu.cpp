//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_taskmenu_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_taskmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(action)
#include <QtGui/qaction.h>
#endif
#include <QtCore/qobject.h>
#include <QtWidgets/qwidget.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A qdesigner_internal::QDesignerTaskMenu that Python can take functions over in. Every qdesigner_internal::QDesignerTaskMenu
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_QDesignerTaskMenuCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_QDesignerTaskMenuCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerTaskMenuCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerTaskMenuCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerTaskMenuCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerTaskMenuCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerTaskMenuCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*Cuteqdesigner_internal_QDesignerTaskMenuCall7)(const void *, int *);
class Cuteqdesigner_internal_QDesignerTaskMenu : public qdesigner_internal::QDesignerTaskMenu {
public:
  using qdesigner_internal::QDesignerTaskMenu::QDesignerTaskMenu;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK26QDesignerTaskMenuExtension19preferredEditActionEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerTaskMenuCall0 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerTaskMenuCall1 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerTaskMenuCall2 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerTaskMenuCall3 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerTaskMenuCall4 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerTaskMenuCall5 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerTaskMenuCall6 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QAction *QDesignerTaskMenuExtension::preferredEditAction() const
  QAction *preferredEditAction() const override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerTaskMenuCall7 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAction *>(given);
    }
    return QDesignerTaskMenuExtension::preferredEditAction();
  }
};

//  const QMetaObject *qdesigner_internal::QDesignerTaskMenu::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal17QDesignerTaskMenu10metaObjectEv(
    const qdesigner_internal::QDesignerTaskMenu *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::QDesignerTaskMenu::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal17QDesignerTaskMenu11qt_metacastEPKc(
    qdesigner_internal::QDesignerTaskMenu *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::QDesignerTaskMenu::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal17QDesignerTaskMenu11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::QDesignerTaskMenu *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::QDesignerTaskMenu::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal17QDesignerTaskMenu2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::QDesignerTaskMenu::tr(s, c, n));
}

//  qdesigner_internal::QDesignerTaskMenu::QDesignerTaskMenu(QWidget *widget,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerTaskMenu *ritual_ZN18qdesigner_internal17QDesignerTaskMenuC1EP7QWidgetP7QObject(
    QWidget *widget,
    QObject *parent) {
  return new Cuteqdesigner_internal_QDesignerTaskMenu(widget, parent);
}

//  qdesigner_internal::QDesignerTaskMenu::~QDesignerTaskMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenuD1Ev(
    qdesigner_internal::QDesignerTaskMenu *self) {
  delete self;
}

//  QWidget *qdesigner_internal::QDesignerTaskMenu::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal17QDesignerTaskMenu6widgetEv(
    const qdesigner_internal::QDesignerTaskMenu *self) {
  return self->widget();
}

//  QList<QAction *> qdesigner_internal::QDesignerTaskMenu::taskActions()
//      const
extern "C" Q_DECL_EXPORT
QList<QAction *> *ritual_ZNK18qdesigner_internal17QDesignerTaskMenu11taskActionsEv(
    const qdesigner_internal::QDesignerTaskMenu *self) {
  return new QList<QAction *>(self->taskActions());
}

//  bool qdesigner_internal::QDesignerTaskMenu::isSlotNavigationEnabled(const
//      QDesignerFormEditorInterface *core)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal17QDesignerTaskMenu23isSlotNavigationEnabledEPK28QDesignerFormEditorInterface(
    const QDesignerFormEditorInterface *core) {
  return qdesigner_internal::QDesignerTaskMenu::isSlotNavigationEnabled(
      core);
}

//  void qdesigner_internal::QDesignerTaskMenu::navigateToSlot(QDesignerFormE
//      ditorInterface *core, QObject *o, const QString &defaultSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu14navigateToSlotEP28QDesignerFormEditorInterfaceP7QObjectRK7QString(
    QDesignerFormEditorInterface *core,
    QObject *o,
    const QString *defaultSignal) {
  qdesigner_internal::QDesignerTaskMenu::navigateToSlot(
      core,
      o,
      *defaultSignal);
}

//  QDesignerFormWindowInterface
//      *qdesigner_internal::QDesignerTaskMenu::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK18qdesigner_internal17QDesignerTaskMenu10formWindowEv(
    const qdesigner_internal::QDesignerTaskMenu *self) {
  return self->formWindow();
}

//  void qdesigner_internal::QDesignerTaskMenu::changeTextProperty(const
//      QString &propertyName, const QString &windowTitle, PropertyMode pm,
//      Qt::TextFormat desiredFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu18changeTextPropertyERK7QStringS3_NS0_12PropertyModeEN2Qt10TextFormatE(
    qdesigner_internal::QDesignerTaskMenu *self,
    const QString *propertyName,
    const QString *windowTitle,
    qdesigner_internal::QDesignerTaskMenu::PropertyMode pm,
    Qt::TextFormat desiredFormat) {
  self->changeTextProperty(*propertyName, *windowTitle, pm, desiredFormat);
}

//  QAction *qdesigner_internal::QDesignerTaskMenu::createSeparator()
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN18qdesigner_internal17QDesignerTaskMenu15createSeparatorEv(
    qdesigner_internal::QDesignerTaskMenu *self) {
  return self->createSeparator();
}

//  QObjectList
//      qdesigner_internal::QDesignerTaskMenu::applicableObjects(const
//      QDesignerFormWindowInterface *fw, PropertyMode pm) const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK18qdesigner_internal17QDesignerTaskMenu17applicableObjectsEPK28QDesignerFormWindowInterfaceNS0_12PropertyModeE(
    const qdesigner_internal::QDesignerTaskMenu *self,
    const QDesignerFormWindowInterface *fw,
    qdesigner_internal::QDesignerTaskMenu::PropertyMode pm) {
  return new QList<QObject *>(self->applicableObjects(fw, pm));
}

//  QWidgetList
//      qdesigner_internal::QDesignerTaskMenu::applicableWidgets(const
//      QDesignerFormWindowInterface *fw, PropertyMode pm) const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK18qdesigner_internal17QDesignerTaskMenu17applicableWidgetsEPK28QDesignerFormWindowInterfaceNS0_12PropertyModeE(
    const qdesigner_internal::QDesignerTaskMenu *self,
    const QDesignerFormWindowInterface *fw,
    qdesigner_internal::QDesignerTaskMenu::PropertyMode pm) {
  return new QList<QWidget *>(self->applicableWidgets(fw, pm));
}

//  void qdesigner_internal::QDesignerTaskMenu::setProperty(QDesignerFormWind
//      owInterface *fw, PropertyMode pm, const QString &name, const QVariant
//      &newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu11setPropertyEP28QDesignerFormWindowInterfaceNS0_12PropertyModeERK7QStringRK8QVariant(
    qdesigner_internal::QDesignerTaskMenu *self,
    QDesignerFormWindowInterface *fw,
    qdesigner_internal::QDesignerTaskMenu::PropertyMode pm,
    const QString *name,
    const QVariant *newValue) {
  self->setProperty(fw, pm, *name, *newValue);
}

//  void qdesigner_internal::QDesignerTaskMenu::changeObjectName()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu16changeObjectNameEv(
    qdesigner_internal::QDesignerTaskMenu *self) {
  self->changeObjectName();
}

//  void qdesigner_internal::QDesignerTaskMenu::changeToolTip()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu13changeToolTipEv(
    qdesigner_internal::QDesignerTaskMenu *self) {
  self->changeToolTip();
}

//  void qdesigner_internal::QDesignerTaskMenu::changeWhatsThis()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu15changeWhatsThisEv(
    qdesigner_internal::QDesignerTaskMenu *self) {
  self->changeWhatsThis();
}

//  void qdesigner_internal::QDesignerTaskMenu::changeStyleSheet()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu16changeStyleSheetEv(
    qdesigner_internal::QDesignerTaskMenu *self) {
  self->changeStyleSheet();
}

//  void qdesigner_internal::QDesignerTaskMenu::createMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu13createMenuBarEv(
    qdesigner_internal::QDesignerTaskMenu *self) {
  self->createMenuBar();
}

//  void qdesigner_internal::QDesignerTaskMenu::addToolBar(Qt::ToolBarArea
//      area)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu10addToolBarEN2Qt11ToolBarAreaE(
    qdesigner_internal::QDesignerTaskMenu *self,
    Qt::ToolBarArea area) {
  self->addToolBar(area);
}

//  void qdesigner_internal::QDesignerTaskMenu::createStatusBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu15createStatusBarEv(
    qdesigner_internal::QDesignerTaskMenu *self) {
  self->createStatusBar();
}

//  void qdesigner_internal::QDesignerTaskMenu::removeStatusBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu15removeStatusBarEv(
    qdesigner_internal::QDesignerTaskMenu *self) {
  self->removeStatusBar();
}

//  void qdesigner_internal::QDesignerTaskMenu::containerFakeMethods()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu20containerFakeMethodsEv(
    qdesigner_internal::QDesignerTaskMenu *self) {
  self->containerFakeMethods();
}

//  void qdesigner_internal::QDesignerTaskMenu::slotNavigateToSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu18slotNavigateToSlotEv(
    qdesigner_internal::QDesignerTaskMenu *self) {
  self->slotNavigateToSlot();
}

//  void qdesigner_internal::QDesignerTaskMenu::applySize(QAction *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu9applySizeEP7QAction(
    qdesigner_internal::QDesignerTaskMenu *self,
    QAction *a) {
  self->applySize(a);
}

//  void qdesigner_internal::QDesignerTaskMenu::slotLayoutAlignment()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17QDesignerTaskMenu19slotLayoutAlignmentEv(
    qdesigner_internal::QDesignerTaskMenu *self) {
  self->slotLayoutAlignment();
}

//  qdesigner_internal::QDesignerTaskMenu as the QDesignerTaskMenuExtension
//      it is built on
extern "C" Q_DECL_EXPORT
QDesignerTaskMenuExtension *ritual_cast_qdesigner_internal_QDesignerTaskMenu_QDesignerTaskMenuExtension(
    qdesigner_internal::QDesignerTaskMenu *self) {
  return static_cast<QDesignerTaskMenuExtension *>(self);
}

//  a Python function taken by a Cuteqdesigner_internal_QDesignerTaskMenu,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_QDesignerTaskMenu(
    qdesigner_internal::QDesignerTaskMenu *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_QDesignerTaskMenu *>(self)->take(key, call);
}
