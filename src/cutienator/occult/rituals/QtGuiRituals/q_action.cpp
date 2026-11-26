//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaction.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by hand,
//  instances of templates of the class: 3. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(action)
#if QT_CONFIG(action)
#include <QtGui/qaction.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qobject.h>
#include <QtGui/qkeysequence.h>
#include <QtGui/qfont.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QAction may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAction : QAction {
  using QAction::event;
};

//  A QAction that Python can take functions over in. Every QAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(action)
typedef bool (*CuteQActionCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(action)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQActionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQActionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQActionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQActionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQActionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQActionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAction : public QAction {
public:
  using QAction::QAction;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(action)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(action)
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
    return false;
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(action)
  //  bool QAction::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQActionCall0 call = reinterpret_cast<CuteQActionCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAction::event(a0);
  }
#endif  // QT_CONFIG(action)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQActionCall1 call = reinterpret_cast<CuteQActionCall1>(taken[1]);
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
      CuteQActionCall2 call = reinterpret_cast<CuteQActionCall2>(taken[2]);
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
      CuteQActionCall3 call = reinterpret_cast<CuteQActionCall3>(taken[3]);
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
      CuteQActionCall4 call = reinterpret_cast<CuteQActionCall4>(taken[4]);
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
      CuteQActionCall5 call = reinterpret_cast<CuteQActionCall5>(taken[5]);
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
      CuteQActionCall6 call = reinterpret_cast<CuteQActionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAction::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QAction10metaObjectEv(const QAction *self) {
  return self->metaObject();
}

//  void *QAction::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN7QAction11qt_metacastEPKc(QAction *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAction::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QAction11qt_metacallEN11QMetaObject4CallEiPPv(
    QAction *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAction::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QAction2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QAction::tr(s, c, n));
}

//  QActionPrivate *QAction::d_func()
extern "C" Q_DECL_EXPORT
QActionPrivate *ritual_ZN7QAction6d_funcEv(QAction *self) {
  return self->d_func();
}

//  const QActionPrivate *QAction::d_func() const
extern "C" Q_DECL_EXPORT
const QActionPrivate *ritual_ZNK7QAction6d_funcEv(const QAction *self) {
  return self->d_func();
}

//  QAction::QAction(QObject *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QActionC1EP7QObject(QObject *parent) {
  return new CuteQAction(parent);
}

//  QAction::QAction(const QString &text, QObject *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QActionC1ERK7QStringP7QObject(
    const QString *text,
    QObject *parent) {
  return new CuteQAction(*text, parent);
}

//  QAction::QAction(const QIcon &icon, const QString &text, QObject *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QActionC1ERK5QIconRK7QStringP7QObject(
    const QIcon *icon,
    const QString *text,
    QObject *parent) {
  return new CuteQAction(*icon, *text, parent);
}

//  QAction::~QAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QActionD1Ev(QAction *self) {
  delete self;
}

//  QList<QObject *> QAction::associatedObjects() const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK7QAction17associatedObjectsEv(
    const QAction *self) {
  return new QList<QObject *>(self->associatedObjects());
}

//  void QAction::setActionGroup(QActionGroup *group)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction14setActionGroupEP12QActionGroup(
    QAction *self,
    QActionGroup *group) {
  self->setActionGroup(group);
}

//  QActionGroup *QAction::actionGroup() const
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_ZNK7QAction11actionGroupEv(const QAction *self) {
  return self->actionGroup();
}

//  void QAction::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction7setIconERK5QIcon(QAction *self, const QIcon *icon) {
  self->setIcon(*icon);
}

//  QIcon QAction::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK7QAction4iconEv(const QAction *self) {
  return new QIcon(self->icon());
}

//  void QAction::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction7setTextERK7QString(
    QAction *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QAction::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QAction4textEv(const QAction *self) {
  return new QString(self->text());
}

//  void QAction::setIconText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction11setIconTextERK7QString(
    QAction *self,
    const QString *text) {
  self->setIconText(*text);
}

//  QString QAction::iconText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QAction8iconTextEv(const QAction *self) {
  return new QString(self->iconText());
}

//  void QAction::setToolTip(const QString &tip)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction10setToolTipERK7QString(
    QAction *self,
    const QString *tip) {
  self->setToolTip(*tip);
}

//  QString QAction::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QAction7toolTipEv(const QAction *self) {
  return new QString(self->toolTip());
}

//  void QAction::setStatusTip(const QString &statusTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction12setStatusTipERK7QString(
    QAction *self,
    const QString *statusTip) {
  self->setStatusTip(*statusTip);
}

//  QString QAction::statusTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QAction9statusTipEv(const QAction *self) {
  return new QString(self->statusTip());
}

//  void QAction::setWhatsThis(const QString &what)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction12setWhatsThisERK7QString(
    QAction *self,
    const QString *what) {
  self->setWhatsThis(*what);
}

//  QString QAction::whatsThis() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QAction9whatsThisEv(const QAction *self) {
  return new QString(self->whatsThis());
}

//  void QAction::setPriority(Priority priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction11setPriorityENS_8PriorityE(
    QAction *self,
    QAction::Priority priority) {
  self->setPriority(priority);
}

//  Priority QAction::priority() const
extern "C" Q_DECL_EXPORT
QAction::Priority ritual_ZNK7QAction8priorityEv(const QAction *self) {
  return self->priority();
}

//  void QAction::setSeparator(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction12setSeparatorEb(QAction *self, bool b) {
  self->setSeparator(b);
}

//  bool QAction::isSeparator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QAction11isSeparatorEv(const QAction *self) {
  return self->isSeparator();
}

#if QT_CONFIG(shortcut)
//  void QAction::setShortcut(const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction11setShortcutERK12QKeySequence(
    QAction *self,
    const QKeySequence *shortcut) {
  self->setShortcut(*shortcut);
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  QKeySequence QAction::shortcut() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK7QAction8shortcutEv(const QAction *self) {
  return new QKeySequence(self->shortcut());
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  void QAction::setShortcuts(const QList<QKeySequence> &shortcuts)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction12setShortcutsERK5QListI12QKeySequenceE(
    QAction *self,
    const QList<QKeySequence> *shortcuts) {
  self->setShortcuts(*shortcuts);
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  void QAction::setShortcuts(QKeySequence::StandardKey a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction12setShortcutsEN12QKeySequence11StandardKeyE(
    QAction *self,
    QKeySequence::StandardKey a0) {
  self->setShortcuts(a0);
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  QList<QKeySequence> QAction::shortcuts() const
extern "C" Q_DECL_EXPORT
QList<QKeySequence> *ritual_ZNK7QAction9shortcutsEv(const QAction *self) {
  return new QList<QKeySequence>(self->shortcuts());
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  void QAction::setShortcutContext(Qt::ShortcutContext context)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction18setShortcutContextEN2Qt15ShortcutContextE(
    QAction *self,
    Qt::ShortcutContext context) {
  self->setShortcutContext(context);
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  Qt::ShortcutContext QAction::shortcutContext() const
extern "C" Q_DECL_EXPORT
Qt::ShortcutContext ritual_ZNK7QAction15shortcutContextEv(
    const QAction *self) {
  return self->shortcutContext();
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  void QAction::setAutoRepeat(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction13setAutoRepeatEb(QAction *self, bool a0) {
  self->setAutoRepeat(a0);
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  bool QAction::autoRepeat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QAction10autoRepeatEv(const QAction *self) {
  return self->autoRepeat();
}
#endif  // QT_CONFIG(shortcut)

//  void QAction::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction7setFontERK5QFont(QAction *self, const QFont *font) {
  self->setFont(*font);
}

//  QFont QAction::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK7QAction4fontEv(const QAction *self) {
  return new QFont(self->font());
}

//  void QAction::setCheckable(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction12setCheckableEb(QAction *self, bool a0) {
  self->setCheckable(a0);
}

//  bool QAction::isCheckable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QAction11isCheckableEv(const QAction *self) {
  return self->isCheckable();
}

//  QVariant QAction::data() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QAction4dataEv(const QAction *self) {
  return new QVariant(self->data());
}

//  void QAction::setData(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction7setDataERK8QVariant(
    QAction *self,
    const QVariant *var) {
  self->setData(*var);
}

//  bool QAction::isChecked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QAction9isCheckedEv(const QAction *self) {
  return self->isChecked();
}

//  bool QAction::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QAction9isEnabledEv(const QAction *self) {
  return self->isEnabled();
}

//  bool QAction::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QAction9isVisibleEv(const QAction *self) {
  return self->isVisible();
}

//  void QAction::activate(ActionEvent event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction8activateENS_11ActionEventE(
    QAction *self,
    QAction::ActionEvent event) {
  self->activate(event);
}

//  void QAction::setMenuRole(MenuRole menuRole)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction11setMenuRoleENS_8MenuRoleE(
    QAction *self,
    QAction::MenuRole menuRole) {
  self->setMenuRole(menuRole);
}

//  MenuRole QAction::menuRole() const
extern "C" Q_DECL_EXPORT
QAction::MenuRole ritual_ZNK7QAction8menuRoleEv(const QAction *self) {
  return self->menuRole();
}

//  void QAction::setIconVisibleInMenu(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction20setIconVisibleInMenuEb(QAction *self, bool visible) {
  self->setIconVisibleInMenu(visible);
}

//  bool QAction::isIconVisibleInMenu() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QAction19isIconVisibleInMenuEv(const QAction *self) {
  return self->isIconVisibleInMenu();
}

//  void QAction::setShortcutVisibleInContextMenu(bool show)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction31setShortcutVisibleInContextMenuEb(
    QAction *self,
    bool show) {
  self->setShortcutVisibleInContextMenu(show);
}

//  bool QAction::isShortcutVisibleInContextMenu() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QAction30isShortcutVisibleInContextMenuEv(
    const QAction *self) {
  return self->isShortcutVisibleInContextMenu();
}

//  bool QAction::showStatusText(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QAction14showStatusTextEP7QObject(
    QAction *self,
    QObject *object) {
  return self->showStatusText(object);
}

//  bool QAction::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QAction5eventEP6QEvent(QAction *self, QEvent *a0) {
  return self->event(a0);
}

//  QAction::QAction(QActionPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QActionC1ER14QActionPrivateP7QObject(
    QActionPrivate *dd,
    QObject *parent) {
  return new CuteQAction(*dd, parent);
}

//  void QAction::trigger()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction7triggerEv(QAction *self) {
  self->trigger();
}

//  void QAction::hover()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction5hoverEv(QAction *self) {
  self->hover();
}

//  void QAction::setChecked(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction10setCheckedEb(QAction *self, bool a0) {
  self->setChecked(a0);
}

//  void QAction::toggle()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction6toggleEv(QAction *self) {
  self->toggle();
}

//  void QAction::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction10setEnabledEb(QAction *self, bool a0) {
  self->setEnabled(a0);
}

//  void QAction::resetEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction12resetEnabledEv(QAction *self) {
  self->resetEnabled();
}

//  void QAction::setDisabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction11setDisabledEb(QAction *self, bool b) {
  self->setDisabled(b);
}

//  void QAction::setVisible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction10setVisibleEb(QAction *self, bool a0) {
  self->setVisible(a0);
}

//  void QAction::changed()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction7changedEv(QAction *self) {
  self->changed();
}

//  void QAction::enabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction14enabledChangedEb(QAction *self, bool enabled) {
  self->enabledChanged(enabled);
}

//  void QAction::checkableChanged(bool checkable)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction16checkableChangedEb(QAction *self, bool checkable) {
  self->checkableChanged(checkable);
}

//  void QAction::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction14visibleChangedEv(QAction *self) {
  self->visibleChanged();
}

//  void QAction::triggered(bool checked)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction9triggeredEb(QAction *self, bool checked) {
  self->triggered(checked);
}

//  void QAction::hovered()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction7hoveredEv(QAction *self) {
  self->hovered();
}

//  void QAction::toggled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction7toggledEb(QAction *self, bool a0) {
  self->toggled(a0);
}

//  QObject *QAction::menuObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK7QAction10menuObjectEv(const QAction *self) {
  return self->menuObject();
}

//  void QAction::setMenuObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction13setMenuObjectEP7QObject(
    QAction *self,
    QObject *object) {
  self->setMenuObject(object);
}

//  a Python function taken by a CuteQAction, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAction(QAction *self, const char *key, void *call) {
  return static_cast<CuteQAction *>(self)->take(key, call);
}

//  bool QAction::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QAction5eventEP6QEvent(QAction *self, QEvent *a0) {
  return static_cast<OwnQAction *>(self)->OwnQAction::event(a0);
}

//  QList<QAction *>::QList()
extern "C" Q_DECL_EXPORT
QList<QAction *> *ritual_list_make_QAction_ptr() {
  return new QList<QAction *>();
}

//  void QList<QAction *>::append(const QAction * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAction_ptr(QList<QAction *> *self, QAction *element) {
  self->append(element);
}

//  qsizetype QList<QAction *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAction_ptr(const QList<QAction *> *self) {
  return self->size();
}

//  const QAction * &QList<QAction *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QAction *ritual_list_at_QAction_ptr(
    const QList<QAction *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QAction *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAction_ptr(QList<QAction *> *self) {
  delete self;
}

//  QObject *QAction::menu<QObject *>() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK7QAction4menuIP7QObjectEET_v(const QAction *self) {
  return self->menu<QObject *>();
}

//  void QAction::setMenu<QObject *>(QObject *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction7setMenuIP7QObjectEEvT_(QAction *self, QObject *m) {
  self->setMenu<QObject *>(m);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QObject *QAction::parentWidget<QObject *>() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK7QAction12parentWidgetIP7QObjectEET_v(
    const QAction *self) {
  return self->parentWidget<QObject *>();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#endif  // QT_CONFIG(action)
#endif  // QT_CONFIG(action)
