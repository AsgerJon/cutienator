//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractformwindowmanager.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtDesigner/abstractformwindowmanager.h>
#include <QtCore/qstring.h>
#include <QtDesigner/abstractdnditem.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerFormWindowManagerInterface that Python can take functions over in. Every QDesignerFormWindowManagerInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerFormWindowManagerInterfaceCall0)(const void *, int, int *);
typedef void * (*CuteQDesignerFormWindowManagerInterfaceCall1)(const void *, int, int *);
typedef void * (*CuteQDesignerFormWindowManagerInterfaceCall2)(const void *, int *);
typedef int (*CuteQDesignerFormWindowManagerInterfaceCall3)(const void *, int *);
typedef void * (*CuteQDesignerFormWindowManagerInterfaceCall4)(const void *, int, int *);
typedef void * (*CuteQDesignerFormWindowManagerInterfaceCall5)(const void *, QWidget *, int, int *);
typedef void * (*CuteQDesignerFormWindowManagerInterfaceCall6)(const void *, int *);
typedef const QPixmap * (*CuteQDesignerFormWindowManagerInterfaceCall7)(const void *, int *);
typedef void (*CuteQDesignerFormWindowManagerInterfaceCall8)(const void *, QDesignerFormWindowInterface *, int *);
typedef void (*CuteQDesignerFormWindowManagerInterfaceCall9)(const void *, QDesignerFormWindowInterface *, int *);
typedef void (*CuteQDesignerFormWindowManagerInterfaceCall10)(const void *, QDesignerFormWindowInterface *, int *);
typedef void (*CuteQDesignerFormWindowManagerInterfaceCall11)(const void *, int *);
typedef void (*CuteQDesignerFormWindowManagerInterfaceCall12)(const void *, int *);
typedef void (*CuteQDesignerFormWindowManagerInterfaceCall13)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerFormWindowManagerInterfaceCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerFormWindowManagerInterfaceCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowManagerInterfaceCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowManagerInterfaceCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowManagerInterfaceCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowManagerInterfaceCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowManagerInterfaceCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerFormWindowManagerInterface : public QDesignerFormWindowManagerInterface {
public:
  using QDesignerFormWindowManagerInterface::QDesignerFormWindowManagerInterface;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface6actionENS_6ActionE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface11actionGroupENS_11ActionGroupE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface16activeFormWindowEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface15formWindowCountEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface10formWindowEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface16createFormWindowEP7QWidget6QFlagsIN2Qt10WindowTypeEE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface4coreEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK35QDesignerFormWindowManagerInterface19createPreviewPixmapEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface13addFormWindowEP28QDesignerFormWindowInterface")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface16removeFormWindowEP28QDesignerFormWindowInterface")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface19setActiveFormWindowEP28QDesignerFormWindowInterface")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface11showPreviewEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface16closeAllPreviewsEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QDesignerFormWindowManagerInterface16showPluginDialogEv")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QAction *QDesignerFormWindowManagerInterface::action(Action action)
  //      const
  QAction *action(
      QDesignerFormWindowManagerInterface::Action action) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall0 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall1 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall1>(taken[1]);
      void * given = call(this, static_cast<int>(actionGroup), &handled);
      if (handled) return static_cast<QActionGroup *>(given);
    }
    return {};
  }

  //  QDesignerFormWindowInterface
  //      *QDesignerFormWindowManagerInterface::activeFormWindow() const
  QDesignerFormWindowInterface *activeFormWindow() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall2 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormWindowInterface *>(given);
    }
    return {};
  }

  //  int QDesignerFormWindowManagerInterface::formWindowCount() const
  int formWindowCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall3 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QDesignerFormWindowInterface
  //      *QDesignerFormWindowManagerInterface::formWindow(int index) const
  QDesignerFormWindowInterface *formWindow(int index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall4 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall5 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall5>(taken[5]);
      void * given = call(this, parentWidget, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QDesignerFormWindowInterface *>(given);
    }
    return {};
  }

  //  QDesignerFormEditorInterface
  //      *QDesignerFormWindowManagerInterface::core() const
  QDesignerFormEditorInterface *core() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall6 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return {};
  }

  //  QPixmap QDesignerFormWindowManagerInterface::createPreviewPixmap()
  //      const
  QPixmap createPreviewPixmap() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall7 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall7>(taken[7]);
      const QPixmap * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QDesignerFormWindowManagerInterface::addFormWindow(QDesignerForm
  //      WindowInterface *formWindow)
  void addFormWindow(QDesignerFormWindowInterface *formWindow) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall8 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall8>(taken[8]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowManagerInterface::removeFormWindow(QDesignerF
  //      ormWindowInterface *formWindow)
  void removeFormWindow(QDesignerFormWindowInterface *formWindow) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall9 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall9>(taken[9]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowManagerInterface::setActiveFormWindow(QDesign
  //      erFormWindowInterface *formWindow)
  void setActiveFormWindow(
      QDesignerFormWindowInterface *formWindow) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall10 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall10>(taken[10]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowManagerInterface::showPreview()
  void showPreview() override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall11 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowManagerInterface::closeAllPreviews()
  void closeAllPreviews() override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall12 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowManagerInterface::showPluginDialog()
  void showPluginDialog() override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall13 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall14 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall15 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall16 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall17 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall18 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall19 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerFormWindowManagerInterfaceCall20 call = reinterpret_cast<CuteQDesignerFormWindowManagerInterfaceCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerFormWindowManagerInterface::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK35QDesignerFormWindowManagerInterface10metaObjectEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->metaObject();
}

//  void *QDesignerFormWindowManagerInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN35QDesignerFormWindowManagerInterface11qt_metacastEPKc(
    QDesignerFormWindowManagerInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerFormWindowManagerInterface::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN35QDesignerFormWindowManagerInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerFormWindowManagerInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerFormWindowManagerInterface::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN35QDesignerFormWindowManagerInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerFormWindowManagerInterface::tr(s, c, n));
}

//  QDesignerFormWindowManagerInterface::~QDesignerFormWindowManagerInterface
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterfaceD1Ev(
    QDesignerFormWindowManagerInterface *self) {
  delete self;
}

//  QAction *QDesignerFormWindowManagerInterface::action(Action action) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface6actionENS_6ActionE(
    const QDesignerFormWindowManagerInterface *self,
    QDesignerFormWindowManagerInterface::Action action) {
  return self->action(action);
}

//  QActionGroup
//      *QDesignerFormWindowManagerInterface::actionGroup(ActionGroup
//      actionGroup) const
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_ZNK35QDesignerFormWindowManagerInterface11actionGroupENS_11ActionGroupE(
    const QDesignerFormWindowManagerInterface *self,
    QDesignerFormWindowManagerInterface::ActionGroup actionGroup) {
  return self->actionGroup(actionGroup);
}

#if QT_CONFIG(clipboard)
//  QAction *QDesignerFormWindowManagerInterface::actionCut() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface9actionCutEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionCut();
}
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(clipboard)
//  QAction *QDesignerFormWindowManagerInterface::actionCopy() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface10actionCopyEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionCopy();
}
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(clipboard)
//  QAction *QDesignerFormWindowManagerInterface::actionPaste() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface11actionPasteEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionPaste();
}
#endif  // QT_CONFIG(clipboard)

//  QAction *QDesignerFormWindowManagerInterface::actionDelete() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface12actionDeleteEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionDelete();
}

//  QAction *QDesignerFormWindowManagerInterface::actionSelectAll() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface15actionSelectAllEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionSelectAll();
}

//  QAction *QDesignerFormWindowManagerInterface::actionLower() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface11actionLowerEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionLower();
}

//  QAction *QDesignerFormWindowManagerInterface::actionRaise() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface11actionRaiseEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionRaise();
}

//  QAction *QDesignerFormWindowManagerInterface::actionUndo() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface10actionUndoEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionUndo();
}

//  QAction *QDesignerFormWindowManagerInterface::actionRedo() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface10actionRedoEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionRedo();
}

//  QAction *QDesignerFormWindowManagerInterface::actionHorizontalLayout()
//      const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface22actionHorizontalLayoutEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionHorizontalLayout();
}

//  QAction *QDesignerFormWindowManagerInterface::actionVerticalLayout()
//      const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface20actionVerticalLayoutEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionVerticalLayout();
}

//  QAction *QDesignerFormWindowManagerInterface::actionSplitHorizontal()
//      const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface21actionSplitHorizontalEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionSplitHorizontal();
}

//  QAction *QDesignerFormWindowManagerInterface::actionSplitVertical() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface19actionSplitVerticalEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionSplitVertical();
}

//  QAction *QDesignerFormWindowManagerInterface::actionGridLayout() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface16actionGridLayoutEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionGridLayout();
}

//  QAction *QDesignerFormWindowManagerInterface::actionFormLayout() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface16actionFormLayoutEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionFormLayout();
}

//  QAction *QDesignerFormWindowManagerInterface::actionBreakLayout() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface17actionBreakLayoutEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionBreakLayout();
}

//  QAction *QDesignerFormWindowManagerInterface::actionAdjustSize() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface16actionAdjustSizeEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionAdjustSize();
}

//  QAction *QDesignerFormWindowManagerInterface::actionSimplifyLayout()
//      const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK35QDesignerFormWindowManagerInterface20actionSimplifyLayoutEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->actionSimplifyLayout();
}

//  QDesignerFormWindowInterface
//      *QDesignerFormWindowManagerInterface::activeFormWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK35QDesignerFormWindowManagerInterface16activeFormWindowEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->activeFormWindow();
}

//  int QDesignerFormWindowManagerInterface::formWindowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK35QDesignerFormWindowManagerInterface15formWindowCountEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->formWindowCount();
}

//  QDesignerFormWindowInterface
//      *QDesignerFormWindowManagerInterface::formWindow(int index) const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK35QDesignerFormWindowManagerInterface10formWindowEi(
    const QDesignerFormWindowManagerInterface *self,
    int index) {
  return self->formWindow(index);
}

//  QDesignerFormWindowInterface
//      *QDesignerFormWindowManagerInterface::createFormWindow(QWidget
//      *parentWidget, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZN35QDesignerFormWindowManagerInterface16createFormWindowEP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QDesignerFormWindowManagerInterface *self,
    QWidget *parentWidget,
    int flags) {
  return self->createFormWindow(
      parentWidget,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QDesignerFormEditorInterface *QDesignerFormWindowManagerInterface::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK35QDesignerFormWindowManagerInterface4coreEv(
    const QDesignerFormWindowManagerInterface *self) {
  return self->core();
}

//  void QDesignerFormWindowManagerInterface::dragItems(const
//      QList<QDesignerDnDItemInterface *> &item_list)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterface9dragItemsERK5QListIP25QDesignerDnDItemInterfaceE(
    QDesignerFormWindowManagerInterface *self,
    const QList<QDesignerDnDItemInterface *> *item_list) {
  self->dragItems(*item_list);
}

//  QPixmap QDesignerFormWindowManagerInterface::createPreviewPixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK35QDesignerFormWindowManagerInterface19createPreviewPixmapEv(
    const QDesignerFormWindowManagerInterface *self) {
  return new QPixmap(self->createPreviewPixmap());
}

//  void QDesignerFormWindowManagerInterface::formWindowAdded(QDesignerFormWi
//      ndowInterface *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterface15formWindowAddedEP28QDesignerFormWindowInterface(
    QDesignerFormWindowManagerInterface *self,
    QDesignerFormWindowInterface *formWindow) {
  self->formWindowAdded(formWindow);
}

//  void QDesignerFormWindowManagerInterface::formWindowRemoved(QDesignerForm
//      WindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterface17formWindowRemovedEP28QDesignerFormWindowInterface(
    QDesignerFormWindowManagerInterface *self,
    QDesignerFormWindowInterface *formWindow) {
  self->formWindowRemoved(formWindow);
}

//  void QDesignerFormWindowManagerInterface::activeFormWindowChanged(QDesign
//      erFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterface23activeFormWindowChangedEP28QDesignerFormWindowInterface(
    QDesignerFormWindowManagerInterface *self,
    QDesignerFormWindowInterface *formWindow) {
  self->activeFormWindowChanged(formWindow);
}

//  void QDesignerFormWindowManagerInterface::formWindowSettingsChanged(QDesi
//      gnerFormWindowInterface *fw)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterface25formWindowSettingsChangedEP28QDesignerFormWindowInterface(
    QDesignerFormWindowManagerInterface *self,
    QDesignerFormWindowInterface *fw) {
  self->formWindowSettingsChanged(fw);
}

//  void QDesignerFormWindowManagerInterface::addFormWindow(QDesignerFormWind
//      owInterface *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterface13addFormWindowEP28QDesignerFormWindowInterface(
    QDesignerFormWindowManagerInterface *self,
    QDesignerFormWindowInterface *formWindow) {
  self->addFormWindow(formWindow);
}

//  void QDesignerFormWindowManagerInterface::removeFormWindow(QDesignerFormW
//      indowInterface *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterface16removeFormWindowEP28QDesignerFormWindowInterface(
    QDesignerFormWindowManagerInterface *self,
    QDesignerFormWindowInterface *formWindow) {
  self->removeFormWindow(formWindow);
}

//  void QDesignerFormWindowManagerInterface::setActiveFormWindow(QDesignerFo
//      rmWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterface19setActiveFormWindowEP28QDesignerFormWindowInterface(
    QDesignerFormWindowManagerInterface *self,
    QDesignerFormWindowInterface *formWindow) {
  self->setActiveFormWindow(formWindow);
}

//  void QDesignerFormWindowManagerInterface::showPreview()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterface11showPreviewEv(
    QDesignerFormWindowManagerInterface *self) {
  self->showPreview();
}

//  void QDesignerFormWindowManagerInterface::closeAllPreviews()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterface16closeAllPreviewsEv(
    QDesignerFormWindowManagerInterface *self) {
  self->closeAllPreviews();
}

//  void QDesignerFormWindowManagerInterface::showPluginDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QDesignerFormWindowManagerInterface16showPluginDialogEv(
    QDesignerFormWindowManagerInterface *self) {
  self->showPluginDialog();
}

//  a Python function taken by a CuteQDesignerFormWindowManagerInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerFormWindowManagerInterface(
    QDesignerFormWindowManagerInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerFormWindowManagerInterface *>(self)->take(key, call);
}
