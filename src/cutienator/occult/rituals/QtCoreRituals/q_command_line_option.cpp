//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcommandlineoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcommandlineoption.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QCommandLineOption::QCommandLineOption(const QString &name)
extern "C" Q_DECL_EXPORT
QCommandLineOption *ritual_ZN18QCommandLineOptionC1ERK7QString(
    const QString *name) {
  return new QCommandLineOption(*name);
}

//  QCommandLineOption::QCommandLineOption(const QStringList &names)
extern "C" Q_DECL_EXPORT
QCommandLineOption *ritual_ZN18QCommandLineOptionC1ERK5QListI7QStringE(
    const QList<QString> *names) {
  return new QCommandLineOption(*names);
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

//  QCommandLineOption::QCommandLineOption(const QStringList &names, const
//      QString &description, const QString &valueName, const QString
//      &defaultValue)
extern "C" Q_DECL_EXPORT
QCommandLineOption *ritual_ZN18QCommandLineOptionC1ERK5QListI7QStringERKS1_S6_S6_(
    const QList<QString> *names,
    const QString *description,
    const QString *valueName,
    const QString *defaultValue) {
  return new QCommandLineOption(
      *names,
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

//  QStringList QCommandLineOption::names() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QCommandLineOption5namesEv(
    const QCommandLineOption *self) {
  return new QList<QString>(self->names());
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

//  void QCommandLineOption::setDefaultValues(const QStringList
//      &defaultValues)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineOption16setDefaultValuesERK5QListI7QStringE(
    QCommandLineOption *self,
    const QList<QString> *defaultValues) {
  self->setDefaultValues(*defaultValues);
}

//  QStringList QCommandLineOption::defaultValues() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QCommandLineOption13defaultValuesEv(
    const QCommandLineOption *self) {
  return new QList<QString>(self->defaultValues());
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

//  QList<QCommandLineOption>::QList()
extern "C" Q_DECL_EXPORT
QList<QCommandLineOption> *ritual_list_make_QCommandLineOption() {
  return new QList<QCommandLineOption>();
}

//  void QList<QCommandLineOption>::append(const QCommandLineOption &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCommandLineOption(
    QList<QCommandLineOption> *self,
    const QCommandLineOption *element) {
  self->append(*element);
}

//  qsizetype QList<QCommandLineOption>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCommandLineOption(
    const QList<QCommandLineOption> *self) {
  return self->size();
}

//  const QCommandLineOption &QList<QCommandLineOption>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QCommandLineOption *ritual_list_at_QCommandLineOption(
    const QList<QCommandLineOption> *self,
    long long index) {
  return new QCommandLineOption(self->at(index));
}

//  QList<QCommandLineOption>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCommandLineOption(QList<QCommandLineOption> *self) {
  delete self;
}
