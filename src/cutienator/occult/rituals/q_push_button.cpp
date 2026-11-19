//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qpushbutton.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qpushbutton.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QPushButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QPushButton10metaObjectEv(
    const QPushButton *self) {
  return self->metaObject();
}

//  QString QPushButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QPushButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPushButton::tr(s, c, n));
}

//  QPushButton::QPushButton(QWidget *parent)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN11QPushButtonC1EP7QWidget(QWidget *parent) {
  return new QPushButton(parent);
}

//  QPushButton::QPushButton(const QString &text, QWidget *parent)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN11QPushButtonC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new QPushButton(*text, parent);
}

//  QPushButton::QPushButton(const QIcon &icon, const QString &text, QWidget
//      *parent)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN11QPushButtonC1ERK5QIconRK7QStringP7QWidget(
    const QIcon *icon,
    const QString *text,
    QWidget *parent) {
  return new QPushButton(*icon, *text, parent);
}

//  QPushButton::~QPushButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButtonD1Ev(QPushButton *self) {
  delete self;
}

//  QSize QPushButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QPushButton8sizeHintEv(const QPushButton *self) {
  return new QSize(self->sizeHint());
}

//  QSize QPushButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QPushButton15minimumSizeHintEv(const QPushButton *self) {
  return new QSize(self->minimumSizeHint());
}

//  bool QPushButton::autoDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPushButton11autoDefaultEv(const QPushButton *self) {
  return self->autoDefault();
}

//  void QPushButton::setAutoDefault(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButton14setAutoDefaultEb(QPushButton *self, bool a0) {
  self->setAutoDefault(a0);
}

//  bool QPushButton::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPushButton9isDefaultEv(const QPushButton *self) {
  return self->isDefault();
}

//  void QPushButton::setDefault(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButton10setDefaultEb(QPushButton *self, bool a0) {
  self->setDefault(a0);
}

//  void QPushButton::setMenu(QMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButton7setMenuEP5QMenu(QPushButton *self, QMenu *menu) {
  self->setMenu(menu);
}

//  QMenu *QPushButton::menu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK11QPushButton4menuEv(const QPushButton *self) {
  return self->menu();
}

//  void QPushButton::setFlat(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButton7setFlatEb(QPushButton *self, bool a0) {
  self->setFlat(a0);
}

//  bool QPushButton::isFlat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPushButton6isFlatEv(const QPushButton *self) {
  return self->isFlat();
}

//  void QPushButton::showMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPushButton8showMenuEv(QPushButton *self) {
  self->showMenu();
}
