//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtoolbutton.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtoolbutton.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QToolButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QToolButton10metaObjectEv(
    const QToolButton *self) {
  return self->metaObject();
}

//  QString QToolButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QToolButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QToolButton::tr(s, c, n));
}

//  QToolButton::QToolButton(QWidget *parent)
extern "C" Q_DECL_EXPORT
QToolButton *ritual_ZN11QToolButtonC1EP7QWidget(QWidget *parent) {
  return new QToolButton(parent);
}

//  QToolButton::~QToolButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButtonD1Ev(QToolButton *self) {
  delete self;
}

//  QSize QToolButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QToolButton8sizeHintEv(const QToolButton *self) {
  return new QSize(self->sizeHint());
}

//  QSize QToolButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QToolButton15minimumSizeHintEv(const QToolButton *self) {
  return new QSize(self->minimumSizeHint());
}

//  Qt::ToolButtonStyle QToolButton::toolButtonStyle() const
extern "C" Q_DECL_EXPORT
Qt::ToolButtonStyle ritual_ZNK11QToolButton15toolButtonStyleEv(
    const QToolButton *self) {
  return self->toolButtonStyle();
}

//  Qt::ArrowType QToolButton::arrowType() const
extern "C" Q_DECL_EXPORT
Qt::ArrowType ritual_ZNK11QToolButton9arrowTypeEv(const QToolButton *self) {
  return self->arrowType();
}

//  void QToolButton::setArrowType(Qt::ArrowType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton12setArrowTypeEN2Qt9ArrowTypeE(
    QToolButton *self,
    Qt::ArrowType type) {
  self->setArrowType(type);
}

//  void QToolButton::setMenu(QMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton7setMenuEP5QMenu(QToolButton *self, QMenu *menu) {
  self->setMenu(menu);
}

//  QMenu *QToolButton::menu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK11QToolButton4menuEv(const QToolButton *self) {
  return self->menu();
}

//  void QToolButton::setPopupMode(ToolButtonPopupMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton12setPopupModeENS_19ToolButtonPopupModeE(
    QToolButton *self,
    QToolButton::ToolButtonPopupMode mode) {
  self->setPopupMode(mode);
}

//  ToolButtonPopupMode QToolButton::popupMode() const
extern "C" Q_DECL_EXPORT
QToolButton::ToolButtonPopupMode ritual_ZNK11QToolButton9popupModeEv(
    const QToolButton *self) {
  return self->popupMode();
}

//  QAction *QToolButton::defaultAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK11QToolButton13defaultActionEv(const QToolButton *self) {
  return self->defaultAction();
}

//  void QToolButton::setAutoRaise(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton12setAutoRaiseEb(QToolButton *self, bool enable) {
  self->setAutoRaise(enable);
}

//  bool QToolButton::autoRaise() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QToolButton9autoRaiseEv(const QToolButton *self) {
  return self->autoRaise();
}

//  void QToolButton::showMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton8showMenuEv(QToolButton *self) {
  self->showMenu();
}

//  void QToolButton::setToolButtonStyle(Qt::ToolButtonStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton18setToolButtonStyleEN2Qt15ToolButtonStyleE(
    QToolButton *self,
    Qt::ToolButtonStyle style) {
  self->setToolButtonStyle(style);
}

//  void QToolButton::setDefaultAction(QAction *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton16setDefaultActionEP7QAction(
    QToolButton *self,
    QAction *a0) {
  self->setDefaultAction(a0);
}
