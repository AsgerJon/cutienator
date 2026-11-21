//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qsystemtrayicon.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qsystemtrayicon.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QSystemTrayIcon::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QSystemTrayIcon10metaObjectEv(
    const QSystemTrayIcon *self) {
  return self->metaObject();
}

//  QString QSystemTrayIcon::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QSystemTrayIcon2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSystemTrayIcon::tr(s, c, n));
}

//  QSystemTrayIcon::QSystemTrayIcon(QObject *parent)
extern "C" Q_DECL_EXPORT
QSystemTrayIcon *ritual_ZN15QSystemTrayIconC1EP7QObject(QObject *parent) {
  return new QSystemTrayIcon(parent);
}

//  QSystemTrayIcon::QSystemTrayIcon(const QIcon &icon, QObject *parent)
extern "C" Q_DECL_EXPORT
QSystemTrayIcon *ritual_ZN15QSystemTrayIconC1ERK5QIconP7QObject(
    const QIcon *icon,
    QObject *parent) {
  return new QSystemTrayIcon(*icon, parent);
}

//  QSystemTrayIcon::~QSystemTrayIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIconD1Ev(QSystemTrayIcon *self) {
  delete self;
}

//  void QSystemTrayIcon::setContextMenu(QMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon14setContextMenuEP5QMenu(
    QSystemTrayIcon *self,
    QMenu *menu) {
  self->setContextMenu(menu);
}

//  QMenu *QSystemTrayIcon::contextMenu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK15QSystemTrayIcon11contextMenuEv(
    const QSystemTrayIcon *self) {
  return self->contextMenu();
}

//  QIcon QSystemTrayIcon::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK15QSystemTrayIcon4iconEv(const QSystemTrayIcon *self) {
  return new QIcon(self->icon());
}

//  void QSystemTrayIcon::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon7setIconERK5QIcon(
    QSystemTrayIcon *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  QString QSystemTrayIcon::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSystemTrayIcon7toolTipEv(const QSystemTrayIcon *self) {
  return new QString(self->toolTip());
}

//  void QSystemTrayIcon::setToolTip(const QString &tip)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon10setToolTipERK7QString(
    QSystemTrayIcon *self,
    const QString *tip) {
  self->setToolTip(*tip);
}

//  bool QSystemTrayIcon::isSystemTrayAvailable()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSystemTrayIcon21isSystemTrayAvailableEv() {
  return QSystemTrayIcon::isSystemTrayAvailable();
}

//  bool QSystemTrayIcon::supportsMessages()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSystemTrayIcon16supportsMessagesEv() {
  return QSystemTrayIcon::supportsMessages();
}

//  QRect QSystemTrayIcon::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QSystemTrayIcon8geometryEv(const QSystemTrayIcon *self) {
  return new QRect(self->geometry());
}

//  bool QSystemTrayIcon::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSystemTrayIcon9isVisibleEv(const QSystemTrayIcon *self) {
  return self->isVisible();
}

//  void QSystemTrayIcon::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon10setVisibleEb(
    QSystemTrayIcon *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QSystemTrayIcon::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon4showEv(QSystemTrayIcon *self) {
  self->show();
}

//  void QSystemTrayIcon::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon4hideEv(QSystemTrayIcon *self) {
  self->hide();
}

//  void QSystemTrayIcon::showMessage(const QString &title, const QString
//      &msg, const QIcon &icon, int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon11showMessageERK7QStringS2_RK5QIconi(
    QSystemTrayIcon *self,
    const QString *title,
    const QString *msg,
    const QIcon *icon,
    int msecs) {
  self->showMessage(*title, *msg, *icon, msecs);
}

//  void QSystemTrayIcon::showMessage(const QString &title, const QString
//      &msg, QSystemTrayIcon::MessageIcon icon, int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSystemTrayIcon11showMessageERK7QStringS2_NS_11MessageIconEi(
    QSystemTrayIcon *self,
    const QString *title,
    const QString *msg,
    QSystemTrayIcon::MessageIcon icon,
    int msecs) {
  self->showMessage(*title, *msg, icon, msecs);
}
