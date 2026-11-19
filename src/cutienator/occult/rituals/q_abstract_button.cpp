//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractbutton.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qabstractbutton.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qsize.h>
#include <QtGui/qkeysequence.h>

//  const QMetaObject *QAbstractButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAbstractButton10metaObjectEv(
    const QAbstractButton *self) {
  return self->metaObject();
}

//  QString QAbstractButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAbstractButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractButton::tr(s, c, n));
}

//  QAbstractButton::~QAbstractButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButtonD1Ev(QAbstractButton *self) {
  delete self;
}

//  void QAbstractButton::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton7setTextERK7QString(
    QAbstractButton *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QAbstractButton::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractButton4textEv(const QAbstractButton *self) {
  return new QString(self->text());
}

//  void QAbstractButton::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton7setIconERK5QIcon(
    QAbstractButton *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  QIcon QAbstractButton::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK15QAbstractButton4iconEv(const QAbstractButton *self) {
  return new QIcon(self->icon());
}

//  QSize QAbstractButton::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QAbstractButton8iconSizeEv(const QAbstractButton *self) {
  return new QSize(self->iconSize());
}

//  void QAbstractButton::setShortcut(const QKeySequence &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton11setShortcutERK12QKeySequence(
    QAbstractButton *self,
    const QKeySequence *key) {
  self->setShortcut(*key);
}

//  QKeySequence QAbstractButton::shortcut() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK15QAbstractButton8shortcutEv(
    const QAbstractButton *self) {
  return new QKeySequence(self->shortcut());
}

//  void QAbstractButton::setCheckable(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton12setCheckableEb(
    QAbstractButton *self,
    bool a0) {
  self->setCheckable(a0);
}

//  bool QAbstractButton::isCheckable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractButton11isCheckableEv(
    const QAbstractButton *self) {
  return self->isCheckable();
}

//  bool QAbstractButton::isChecked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractButton9isCheckedEv(const QAbstractButton *self) {
  return self->isChecked();
}

//  void QAbstractButton::setDown(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton7setDownEb(QAbstractButton *self, bool a0) {
  self->setDown(a0);
}

//  bool QAbstractButton::isDown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractButton6isDownEv(const QAbstractButton *self) {
  return self->isDown();
}

//  void QAbstractButton::setAutoRepeat(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton13setAutoRepeatEb(
    QAbstractButton *self,
    bool a0) {
  self->setAutoRepeat(a0);
}

//  bool QAbstractButton::autoRepeat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractButton10autoRepeatEv(const QAbstractButton *self) {
  return self->autoRepeat();
}

//  void QAbstractButton::setAutoRepeatDelay(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton18setAutoRepeatDelayEi(
    QAbstractButton *self,
    int a0) {
  self->setAutoRepeatDelay(a0);
}

//  int QAbstractButton::autoRepeatDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractButton15autoRepeatDelayEv(
    const QAbstractButton *self) {
  return self->autoRepeatDelay();
}

//  void QAbstractButton::setAutoRepeatInterval(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton21setAutoRepeatIntervalEi(
    QAbstractButton *self,
    int a0) {
  self->setAutoRepeatInterval(a0);
}

//  int QAbstractButton::autoRepeatInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractButton18autoRepeatIntervalEv(
    const QAbstractButton *self) {
  return self->autoRepeatInterval();
}

//  void QAbstractButton::setAutoExclusive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton16setAutoExclusiveEb(
    QAbstractButton *self,
    bool a0) {
  self->setAutoExclusive(a0);
}

//  bool QAbstractButton::autoExclusive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractButton13autoExclusiveEv(
    const QAbstractButton *self) {
  return self->autoExclusive();
}

//  QButtonGroup *QAbstractButton::group() const
extern "C" Q_DECL_EXPORT
QButtonGroup *ritual_ZNK15QAbstractButton5groupEv(
    const QAbstractButton *self) {
  return self->group();
}

//  void QAbstractButton::setIconSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton11setIconSizeERK5QSize(
    QAbstractButton *self,
    const QSize *size) {
  self->setIconSize(*size);
}

//  void QAbstractButton::animateClick()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton12animateClickEv(QAbstractButton *self) {
  self->animateClick();
}

//  void QAbstractButton::click()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton5clickEv(QAbstractButton *self) {
  self->click();
}

//  void QAbstractButton::toggle()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton6toggleEv(QAbstractButton *self) {
  self->toggle();
}

//  void QAbstractButton::setChecked(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractButton10setCheckedEb(
    QAbstractButton *self,
    bool a0) {
  self->setChecked(a0);
}
