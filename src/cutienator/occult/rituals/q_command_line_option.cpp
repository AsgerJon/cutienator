//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcommandlineoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcommandlineoption.h>
#include <QtCore/qstring.h>

//  QCommandLineOption::QCommandLineOption(const QString &name)
extern "C" Q_DECL_EXPORT
QCommandLineOption *ritual_ZN18QCommandLineOptionC1ERK7QString(
    const QString *name) {
  return new QCommandLineOption(*name);
}

//  QCommandLineOption::QCommandLineOption(const QString &name, const QString
//      &description, const QString &valueName, const QString &defaultValue)
extern "C" Q_DECL_EXPORT
QCommandLineOption *ritual_ZN18QCommandLineOptionC1ERK7QStringS2_S2_S2_(
    const QString *name,
    const QString *description,
    const QString *valueName,
    const QString *defaultValue) {
  return new QCommandLineOption(
      *name,
      *description,
      *valueName,
      *defaultValue);
}

//  QCommandLineOption::QCommandLineOption(const QCommandLineOption &other)
extern "C" Q_DECL_EXPORT
QCommandLineOption *ritual_ZN18QCommandLineOptionC1ERKS_(
    const QCommandLineOption *other) {
  return new QCommandLineOption(*other);
}

//  QCommandLineOption::~QCommandLineOption()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineOptionD1Ev(QCommandLineOption *self) {
  delete self;
}

//  void QCommandLineOption::setValueName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineOption12setValueNameERK7QString(
    QCommandLineOption *self,
    const QString *name) {
  self->setValueName(*name);
}

//  QString QCommandLineOption::valueName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCommandLineOption9valueNameEv(
    const QCommandLineOption *self) {
  return new QString(self->valueName());
}

//  void QCommandLineOption::setDescription(const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineOption14setDescriptionERK7QString(
    QCommandLineOption *self,
    const QString *description) {
  self->setDescription(*description);
}

//  QString QCommandLineOption::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCommandLineOption11descriptionEv(
    const QCommandLineOption *self) {
  return new QString(self->description());
}

//  void QCommandLineOption::setDefaultValue(const QString &defaultValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineOption15setDefaultValueERK7QString(
    QCommandLineOption *self,
    const QString *defaultValue) {
  self->setDefaultValue(*defaultValue);
}

//  Flags QCommandLineOption::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QCommandLineOption5flagsEv(const QCommandLineOption *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QCommandLineOption::setFlags(Flags aflags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineOption8setFlagsE6QFlagsINS_4FlagEE(
    QCommandLineOption *self,
    int aflags) {
  self->setFlags(QFlags<QCommandLineOption::Flag>::fromInt(aflags));
}
