//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcommandlineparser.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcommandlineparser.h>
#include <QtCore/qstring.h>
#include <QtCore/qcommandlineoption.h>

//  QString QCommandLineParser::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QCommandLineParser2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QCommandLineParser::tr(sourceText, disambiguation, n));
}

//  QCommandLineParser::QCommandLineParser()
extern "C" Q_DECL_EXPORT
QCommandLineParser *ritual_ZN18QCommandLineParserC1Ev() {
  return new QCommandLineParser();
}

//  QCommandLineParser::~QCommandLineParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineParserD1Ev(QCommandLineParser *self) {
  delete self;
}

//  void
//      QCommandLineParser::setSingleDashWordOptionMode(SingleDashWordOptionM
//      ode parsingMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineParser27setSingleDashWordOptionModeENS_24SingleDashWordOptionModeE(
    QCommandLineParser *self,
    QCommandLineParser::SingleDashWordOptionMode parsingMode) {
  self->setSingleDashWordOptionMode(parsingMode);
}

//  void QCommandLineParser::setOptionsAfterPositionalArgumentsMode(OptionsAf
//      terPositionalArgumentsMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineParser38setOptionsAfterPositionalArgumentsModeENS_35OptionsAfterPositionalArgumentsModeE(
    QCommandLineParser *self,
    QCommandLineParser::OptionsAfterPositionalArgumentsMode mode) {
  self->setOptionsAfterPositionalArgumentsMode(mode);
}

//  bool QCommandLineParser::addOption(const QCommandLineOption
//      &commandLineOption)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCommandLineParser9addOptionERK18QCommandLineOption(
    QCommandLineParser *self,
    const QCommandLineOption *commandLineOption) {
  return self->addOption(*commandLineOption);
}

//  QCommandLineOption QCommandLineParser::addVersionOption()
extern "C" Q_DECL_EXPORT
QCommandLineOption *ritual_ZN18QCommandLineParser16addVersionOptionEv(
    QCommandLineParser *self) {
  return new QCommandLineOption(self->addVersionOption());
}

//  QCommandLineOption QCommandLineParser::addHelpOption()
extern "C" Q_DECL_EXPORT
QCommandLineOption *ritual_ZN18QCommandLineParser13addHelpOptionEv(
    QCommandLineParser *self) {
  return new QCommandLineOption(self->addHelpOption());
}

//  void QCommandLineParser::setApplicationDescription(const QString
//      &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineParser25setApplicationDescriptionERK7QString(
    QCommandLineParser *self,
    const QString *description) {
  self->setApplicationDescription(*description);
}

//  QString QCommandLineParser::applicationDescription() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCommandLineParser22applicationDescriptionEv(
    const QCommandLineParser *self) {
  return new QString(self->applicationDescription());
}

//  void QCommandLineParser::addPositionalArgument(const QString &name, const
//      QString &description, const QString &syntax)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineParser21addPositionalArgumentERK7QStringS2_S2_(
    QCommandLineParser *self,
    const QString *name,
    const QString *description,
    const QString *syntax) {
  self->addPositionalArgument(*name, *description, *syntax);
}

//  void QCommandLineParser::clearPositionalArguments()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineParser24clearPositionalArgumentsEv(
    QCommandLineParser *self) {
  self->clearPositionalArguments();
}

//  QString QCommandLineParser::errorText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCommandLineParser9errorTextEv(
    const QCommandLineParser *self) {
  return new QString(self->errorText());
}

//  bool QCommandLineParser::isSet(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCommandLineParser5isSetERK7QString(
    const QCommandLineParser *self,
    const QString *name) {
  return self->isSet(*name);
}

//  QString QCommandLineParser::value(const QString &name) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCommandLineParser5valueERK7QString(
    const QCommandLineParser *self,
    const QString *name) {
  return new QString(self->value(*name));
}

//  bool QCommandLineParser::isSet(const QCommandLineOption &option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCommandLineParser5isSetERK18QCommandLineOption(
    const QCommandLineParser *self,
    const QCommandLineOption *option) {
  return self->isSet(*option);
}

//  QString QCommandLineParser::value(const QCommandLineOption &option) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCommandLineParser5valueERK18QCommandLineOption(
    const QCommandLineParser *self,
    const QCommandLineOption *option) {
  return new QString(self->value(*option));
}

//  void QCommandLineParser::showVersion()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineParser11showVersionEv(QCommandLineParser *self) {
  self->showVersion();
}

//  void QCommandLineParser::showHelp(int exitCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineParser8showHelpEi(
    QCommandLineParser *self,
    int exitCode) {
  self->showHelp(exitCode);
}

//  QString QCommandLineParser::helpText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCommandLineParser8helpTextEv(
    const QCommandLineParser *self) {
  return new QString(self->helpText());
}

//  void QCommandLineParser::showMessageAndExit(MessageType type, const
//      QString &message, int exitCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCommandLineParser18showMessageAndExitENS_11MessageTypeERK7QStringi(
    QCommandLineParser::MessageType type,
    const QString *message,
    int exitCode) {
  QCommandLineParser::showMessageAndExit(type, *message, exitCode);
}
