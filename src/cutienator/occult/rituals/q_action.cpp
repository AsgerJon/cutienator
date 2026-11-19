//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaction.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaction.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/qkeysequence.h>
#include <QtGui/qfont.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QAction::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QAction10metaObjectEv(const QAction *self) {
  return self->metaObject();
}

//  QString QAction::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QAction2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QAction::tr(s, c, n));
}

//  QAction::QAction(QObject *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QActionC1EP7QObject(QObject *parent) {
  return new QAction(parent);
}

//  QAction::QAction(const QString &text, QObject *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QActionC1ERK7QStringP7QObject(
    const QString *text,
    QObject *parent) {
  return new QAction(*text, parent);
}

//  QAction::QAction(const QIcon &icon, const QString &text, QObject *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QActionC1ERK5QIconRK7QStringP7QObject(
    const QIcon *icon,
    const QString *text,
    QObject *parent) {
  return new QAction(*icon, *text, parent);
}

//  QAction::~QAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QActionD1Ev(QAction *self) {
  delete self;
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

//  void QAction::setShortcut(const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction11setShortcutERK12QKeySequence(
    QAction *self,
    const QKeySequence *shortcut) {
  self->setShortcut(*shortcut);
}

//  QKeySequence QAction::shortcut() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK7QAction8shortcutEv(const QAction *self) {
  return new QKeySequence(self->shortcut());
}

//  void QAction::setShortcuts(QKeySequence::StandardKey a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction12setShortcutsEN12QKeySequence11StandardKeyE(
    QAction *self,
    QKeySequence::StandardKey a0) {
  self->setShortcuts(a0);
}

//  void QAction::setShortcutContext(Qt::ShortcutContext context)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction18setShortcutContextEN2Qt15ShortcutContextE(
    QAction *self,
    Qt::ShortcutContext context) {
  self->setShortcutContext(context);
}

//  Qt::ShortcutContext QAction::shortcutContext() const
extern "C" Q_DECL_EXPORT
Qt::ShortcutContext ritual_ZNK7QAction15shortcutContextEv(
    const QAction *self) {
  return self->shortcutContext();
}

//  void QAction::setAutoRepeat(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QAction13setAutoRepeatEb(QAction *self, bool a0) {
  self->setAutoRepeat(a0);
}

//  bool QAction::autoRepeat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QAction10autoRepeatEv(const QAction *self) {
  return self->autoRepeat();
}

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
