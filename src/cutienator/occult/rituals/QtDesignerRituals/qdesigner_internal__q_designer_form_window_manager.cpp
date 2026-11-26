//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_formwindowmanager_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_formwindowmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A qdesigner_internal::QDesignerFormWindowManager that Python can take functions over in. Every qdesigner_internal::QDesignerFormWindowManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall0)(const void *, int *);
typedef void (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall1)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall2)(const void *, int, int *);
typedef void * (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall3)(const void *, int, int *);
typedef void * (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall4)(const void *, int *);
typedef int (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall5)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall6)(const void *, int, int *);
typedef void * (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall7)(const void *, QWidget *, int, int *);
typedef void * (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall8)(const void *, int *);
typedef const QPixmap * (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall9)(const void *, int *);
typedef void (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall10)(const void *, QDesignerFormWindowInterface *, int *);
typedef void (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall11)(const void *, QDesignerFormWindowInterface *, int *);
typedef void (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall12)(const void *, QDesignerFormWindowInterface *, int *);
typedef void (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall13)(const void *, int *);
typedef void (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall14)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall16)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall17)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall18)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerFormWindowManagerCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_QDesignerFormWindowManager : public qdesigner_internal::QDesignerFormWindowManager {
public:
  using qdesigner_internal::QDesignerFormWindowManager::QDesignerFormWindowManager;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18qdesigner_internal26QDesignerFormWindowManager14previewManagerEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface16showPluginDialogEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface6actionENS_6ActionE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface11actionGroupENS_11ActionGroupE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface16activeFormWindowEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface15formWindowCountEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface10formWindowEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface16createFormWindowEP7QWidget6QFlagsIN2Qt10WindowTypeEE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface4coreEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface19createPreviewPixmapEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface13addFormWindowEP28QDesignerFormWindowInterface")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface16removeFormWindowEP28QDesignerFormWindowInterface")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface19setActiveFormWindowEP28QDesignerFormWindowInterface")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface11showPreviewEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface16closeAllPreviewsEv")) {
      taken[14] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  PreviewManager
  //      *qdesigner_internal::QDesignerFormWindowManager::previewManager()
  //      const
  qdesigner_internal::PreviewManager *previewManager() const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall0 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<qdesigner_internal::PreviewManager *>(given);
    }
    return {};
  }

  //  void
  //      qdesigner_internal::QDesignerFormWindowManager::showPluginDialog(
  //      )
  void showPluginDialog() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall1 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::QDesignerFormWindowManager::showPluginDialog();
  }

  //  QAction *QDesignerFormWindowManagerInterface::action(Action action)
  //      const
  QAction *action(
      QDesignerFormWindowManagerInterface::Action action) const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall2 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall2>(taken[2]);
      void * given = call(this, static_cast<int>(action), &handled);
      if (handled) return static_cast<QAction *>(given);
    }
    return {};
  }

  //  QActionGroup
  //      *QDesignerFormWindowManagerInterface::actionGroup(ActionGroup
  //      actionGroup) const
  QActionGroup *actionGroup(
      QDesignerFormWindowManagerInterface::ActionGroup actionGroup) const override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall3 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall3>(taken[3]);
      void * given = call(this, static_cast<int>(actionGroup), &handled);
      if (handled) return static_cast<QActionGroup *>(given);
    }
    return {};
  }

  //  QDesignerFormWindowInterface
  //      *QDesignerFormWindowManagerInterface::activeFormWindow() const
  QDesignerFormWindowInterface *activeFormWindow() const override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall4 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormWindowInterface *>(given);
    }
    return {};
  }

  //  int QDesignerFormWindowManagerInterface::formWindowCount() const
  int formWindowCount() const override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall5 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QDesignerFormWindowInterface
  //      *QDesignerFormWindowManagerInterface::formWindow(int index) const
  QDesignerFormWindowInterface *formWindow(int index) const override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall6 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall6>(taken[6]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QDesignerFormWindowInterface *>(given);
    }
    return {};
  }

  //  QDesignerFormWindowInterface
  //      *QDesignerFormWindowManagerInterface::createFormWindow(QWidget
  //      *parentWidget, Qt::WindowFlags flags)
  QDesignerFormWindowInterface *createFormWindow(
      QWidget *parentWidget,
      Qt::WindowFlags flags) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall7 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall7>(taken[7]);
      void * given = call(this, parentWidget, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QDesignerFormWindowInterface *>(given);
    }
    return {};
  }

  //  QDesignerFormEditorInterface
  //      *QDesignerFormWindowManagerInterface::core() const
  QDesignerFormEditorInterface *core() const override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall8 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return {};
  }

  //  QPixmap QDesignerFormWindowManagerInterface::createPreviewPixmap()
  //      const
  QPixmap createPreviewPixmap() const override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall9 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall9>(taken[9]);
      const QPixmap * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QDesignerFormWindowManagerInterface::addFormWindow(QDesignerForm
  //      WindowInterface *formWindow)
  void addFormWindow(QDesignerFormWindowInterface *formWindow) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall10 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall10>(taken[10]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowManagerInterface::removeFormWindow(QDesignerF
  //      ormWindowInterface *formWindow)
  void removeFormWindow(QDesignerFormWindowInterface *formWindow) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall11 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall11>(taken[11]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowManagerInterface::setActiveFormWindow(QDesign
  //      erFormWindowInterface *formWindow)
  void setActiveFormWindow(
      QDesignerFormWindowInterface *formWindow) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall12 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall12>(taken[12]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowManagerInterface::showPreview()
  void showPreview() override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall13 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowManagerInterface::closeAllPreviews()
  void closeAllPreviews() override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall14 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall15 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall15>(taken[15]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall16 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall16>(taken[16]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall17 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall18 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall19 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall20 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerFormWindowManagerCall21 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerFormWindowManagerCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *qdesigner_internal::QDesignerFormWindowManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal26QDesignerFormWindowManager10metaObjectEv(
    const qdesigner_internal::QDesignerFormWindowManager *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::QDesignerFormWindowManager::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal26QDesignerFormWindowManager11qt_metacastEPKc(
    qdesigner_internal::QDesignerFormWindowManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::QDesignerFormWindowManager::qt_metacall(QMetaObje
//      ct::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal26QDesignerFormWindowManager11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::QDesignerFormWindowManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::QDesignerFormWindowManager::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal26QDesignerFormWindowManager2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      qdesigner_internal::QDesignerFormWindowManager::tr(
          s,
          c,
          n));
}

//  qdesigner_internal::QDesignerFormWindowManager::~QDesignerFormWindowManag
//      er()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal26QDesignerFormWindowManagerD1Ev(
    qdesigner_internal::QDesignerFormWindowManager *self) {
  delete self;
}

//  PreviewManager
//      *qdesigner_internal::QDesignerFormWindowManager::previewManager()
//      const
extern "C" Q_DECL_EXPORT
qdesigner_internal::PreviewManager *ritual_ZNK18qdesigner_internal26QDesignerFormWindowManager14previewManagerEv(
    const qdesigner_internal::QDesignerFormWindowManager *self) {
  return self->previewManager();
}

//  void qdesigner_internal::QDesignerFormWindowManager::showPluginDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal26QDesignerFormWindowManager16showPluginDialogEv(
    qdesigner_internal::QDesignerFormWindowManager *self) {
  self->showPluginDialog();
}

//  a Python function taken by a
//      Cuteqdesigner_internal_QDesignerFormWindowManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_QDesignerFormWindowManager(
    qdesigner_internal::QDesignerFormWindowManager *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_QDesignerFormWindowManager *>(self)->take(key, call);
}

//  void qdesigner_internal::QDesignerFormWindowManager::showPluginDialog()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal26QDesignerFormWindowManager16showPluginDialogEv(
    qdesigner_internal::QDesignerFormWindowManager *self) {
  self->qdesigner_internal::QDesignerFormWindowManager::showPluginDialog();
}
