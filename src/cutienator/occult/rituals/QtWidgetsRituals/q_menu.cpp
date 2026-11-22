//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmenu.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qmenu.h>
#include <QtCore/qstring.h>
#include <QtGui/qkeysequence.h>
#include <QtGui/qicon.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5QMenu10metaObjectEv(const QMenu *self) {
  return self->metaObject();
}

//  QString QMenu::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QMenu2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QMenu::tr(s, c, n));
}

//  QMenu::QMenu(QWidget *parent)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN5QMenuC1EP7QWidget(QWidget *parent) {
  return new QMenu(parent);
}

//  QMenu::QMenu(const QString &title, QWidget *parent)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN5QMenuC1ERK7QStringP7QWidget(
    const QString *title,
    QWidget *parent) {
  return new QMenu(*title, parent);
}

//  QMenu::~QMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenuD1Ev(QMenu *self) {
  delete self;
}

//  QAction *QMenu::addAction(const QString &text, const QObject *receiver,
//      const char *member, const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu9addActionERK7QStringPK7QObjectPKcRK12QKeySequence(
    QMenu *self,
    const QString *text,
    const QObject *receiver,
    const char *member,
    const QKeySequence *shortcut) {
  return self->addAction(*text, receiver, member, *shortcut);
}

//  QAction *QMenu::addAction(const QIcon &icon, const QString &text, const
//      QObject *receiver, const char *member, const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu9addActionERK5QIconRK7QStringPK7QObjectPKcRK12QKeySequence(
    QMenu *self,
    const QIcon *icon,
    const QString *text,
    const QObject *receiver,
    const char *member,
    const QKeySequence *shortcut) {
  return self->addAction(*icon, *text, receiver, member, *shortcut);
}

//  QAction *QMenu::addMenu(QMenu *menu)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu7addMenuEPS_(QMenu *self, QMenu *menu) {
  return self->addMenu(menu);
}

//  QMenu *QMenu::addMenu(const QString &title)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN5QMenu7addMenuERK7QString(
    QMenu *self,
    const QString *title) {
  return self->addMenu(*title);
}

//  QMenu *QMenu::addMenu(const QIcon &icon, const QString &title)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN5QMenu7addMenuERK5QIconRK7QString(
    QMenu *self,
    const QIcon *icon,
    const QString *title) {
  return self->addMenu(*icon, *title);
}

//  QAction *QMenu::addSeparator()
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu12addSeparatorEv(QMenu *self) {
  return self->addSeparator();
}

//  QAction *QMenu::addSection(const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu10addSectionERK7QString(
    QMenu *self,
    const QString *text) {
  return self->addSection(*text);
}

//  QAction *QMenu::addSection(const QIcon &icon, const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu10addSectionERK5QIconRK7QString(
    QMenu *self,
    const QIcon *icon,
    const QString *text) {
  return self->addSection(*icon, *text);
}

//  QAction *QMenu::insertMenu(QAction *before, QMenu *menu)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu10insertMenuEP7QActionPS_(
    QMenu *self,
    QAction *before,
    QMenu *menu) {
  return self->insertMenu(before, menu);
}

//  QAction *QMenu::insertSeparator(QAction *before)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu15insertSeparatorEP7QAction(
    QMenu *self,
    QAction *before) {
  return self->insertSeparator(before);
}

//  QAction *QMenu::insertSection(QAction *before, const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu13insertSectionEP7QActionRK7QString(
    QMenu *self,
    QAction *before,
    const QString *text) {
  return self->insertSection(before, *text);
}

//  QAction *QMenu::insertSection(QAction *before, const QIcon &icon, const
//      QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu13insertSectionEP7QActionRK5QIconRK7QString(
    QMenu *self,
    QAction *before,
    const QIcon *icon,
    const QString *text) {
  return self->insertSection(before, *icon, *text);
}

//  bool QMenu::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QMenu7isEmptyEv(const QMenu *self) {
  return self->isEmpty();
}

//  void QMenu::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu5clearEv(QMenu *self) {
  self->clear();
}

//  void QMenu::setTearOffEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu17setTearOffEnabledEb(QMenu *self, bool a0) {
  self->setTearOffEnabled(a0);
}

//  bool QMenu::isTearOffEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QMenu16isTearOffEnabledEv(const QMenu *self) {
  return self->isTearOffEnabled();
}

//  bool QMenu::isTearOffMenuVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QMenu20isTearOffMenuVisibleEv(const QMenu *self) {
  return self->isTearOffMenuVisible();
}

//  void QMenu::showTearOffMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu15showTearOffMenuEv(QMenu *self) {
  self->showTearOffMenu();
}

//  void QMenu::showTearOffMenu(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu15showTearOffMenuERK6QPoint(
    QMenu *self,
    const QPoint *pos) {
  self->showTearOffMenu(*pos);
}

//  void QMenu::hideTearOffMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu15hideTearOffMenuEv(QMenu *self) {
  self->hideTearOffMenu();
}

//  void QMenu::setDefaultAction(QAction *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu16setDefaultActionEP7QAction(QMenu *self, QAction *a0) {
  self->setDefaultAction(a0);
}

//  QAction *QMenu::defaultAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK5QMenu13defaultActionEv(const QMenu *self) {
  return self->defaultAction();
}

//  void QMenu::setActiveAction(QAction *act)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu15setActiveActionEP7QAction(QMenu *self, QAction *act) {
  self->setActiveAction(act);
}

//  QAction *QMenu::activeAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK5QMenu12activeActionEv(const QMenu *self) {
  return self->activeAction();
}

//  void QMenu::popup(const QPoint &pos, QAction *at)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu5popupERK6QPointP7QAction(
    QMenu *self,
    const QPoint *pos,
    QAction *at) {
  self->popup(*pos, at);
}

//  QAction *QMenu::exec()
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu4execEv(QMenu *self) {
  return self->exec();
}

//  QAction *QMenu::exec(const QPoint &pos, QAction *at)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN5QMenu4execERK6QPointP7QAction(
    QMenu *self,
    const QPoint *pos,
    QAction *at) {
  return self->exec(*pos, at);
}

//  QSize QMenu::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QMenu8sizeHintEv(const QMenu *self) {
  return new QSize(self->sizeHint());
}

//  QRect QMenu::actionGeometry(QAction *a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QMenu14actionGeometryEP7QAction(
    const QMenu *self,
    QAction *a0) {
  return new QRect(self->actionGeometry(a0));
}

//  QAction *QMenu::actionAt(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK5QMenu8actionAtERK6QPoint(
    const QMenu *self,
    const QPoint *a0) {
  return self->actionAt(*a0);
}

//  QAction *QMenu::menuAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK5QMenu10menuActionEv(const QMenu *self) {
  return self->menuAction();
}

//  QMenu *QMenu::menuInAction(const QAction *action)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN5QMenu12menuInActionEPK7QAction(const QAction *action) {
  return QMenu::menuInAction(action);
}

//  QString QMenu::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QMenu5titleEv(const QMenu *self) {
  return new QString(self->title());
}

//  void QMenu::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu8setTitleERK7QString(QMenu *self, const QString *title) {
  self->setTitle(*title);
}

//  QIcon QMenu::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK5QMenu4iconEv(const QMenu *self) {
  return new QIcon(self->icon());
}

//  void QMenu::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu7setIconERK5QIcon(QMenu *self, const QIcon *icon) {
  self->setIcon(*icon);
}

//  void QMenu::setNoReplayFor(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu14setNoReplayForEP7QWidget(
    QMenu *self,
    QWidget *widget) {
  self->setNoReplayFor(widget);
}

//  bool QMenu::separatorsCollapsible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QMenu21separatorsCollapsibleEv(const QMenu *self) {
  return self->separatorsCollapsible();
}

//  void QMenu::setSeparatorsCollapsible(bool collapse)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu24setSeparatorsCollapsibleEb(
    QMenu *self,
    bool collapse) {
  self->setSeparatorsCollapsible(collapse);
}

//  bool QMenu::toolTipsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QMenu15toolTipsVisibleEv(const QMenu *self) {
  return self->toolTipsVisible();
}

//  void QMenu::setToolTipsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QMenu18setToolTipsVisibleEb(QMenu *self, bool visible) {
  self->setToolTipsVisible(visible);
}
