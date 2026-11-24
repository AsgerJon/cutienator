//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/abstractdialoggui_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/abstractdialoggui_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerDialogGuiInterface that Python can take functions over in. Every QDesignerDialogGuiInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQDesignerDialogGuiInterfaceCall0)(const void *, QWidget *, int, int, const QString *, const QString *, int, int, int *);
typedef int (*CuteQDesignerDialogGuiInterfaceCall1)(const void *, QWidget *, int, int, const QString *, const QString *, const QString *, int, int, int *);
typedef int (*CuteQDesignerDialogGuiInterfaceCall2)(const void *, QWidget *, int, int, const QString *, const QString *, const QString *, const QString *, int, int, int *);
typedef QString * (*CuteQDesignerDialogGuiInterfaceCall3)(const void *, QWidget *, const QString *, const QString *, int, int *);
typedef QString * (*CuteQDesignerDialogGuiInterfaceCall4)(const void *, QWidget *, const QString *, const QString *, const QString *, QString *, int, int *);
typedef QString * (*CuteQDesignerDialogGuiInterfaceCall5)(const void *, QWidget *, const QString *, const QString *, const QString *, QString *, int, int *);
typedef QString * (*CuteQDesignerDialogGuiInterfaceCall6)(const void *, QWidget *, const QString *, const QString *, const QString *, QString *, int, int *);
class CuteQDesignerDialogGuiInterface : public QDesignerDialogGuiInterface {
public:
  using QDesignerDialogGuiInterface::QDesignerDialogGuiInterface;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7MessageEN11QMessageBox4IconERK7QStringS7_6QFlagsINS3_14StandardButtonEES9_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7MessageEN11QMessageBox4IconERK7QStringS7_S7_6QFlagsINS3_14StandardButtonEES9_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7MessageEN11QMessageBox4IconERK7QStringS7_S7_S7_6QFlagsINS3_14StandardButtonEES9_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerDialogGuiInterface20getExistingDirectoryEP7QWidgetRK7QStringS4_6QFlagsIN11QFileDialog6OptionEE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerDialogGuiInterface15getOpenFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerDialogGuiInterface20getOpenImageFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerDialogGuiInterface15getSaveFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QMessageBox::StandardButton
  //      QDesignerDialogGuiInterface::message(QWidget *parent, Message
  //      context, QMessageBox::Icon icon, const QString &title, const
  //      QString &text, QMessageBox::StandardButtons buttons,
  //      QMessageBox::StandardButton defaultButton)
  QMessageBox::StandardButton message(
      QWidget *parent,
      QDesignerDialogGuiInterface::Message context,
      QMessageBox::Icon icon,
      const QString &title,
      const QString &text,
      QMessageBox::StandardButtons buttons,
      QMessageBox::StandardButton defaultButton) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerDialogGuiInterfaceCall0 call = reinterpret_cast<CuteQDesignerDialogGuiInterfaceCall0>(taken[0]);
      int given = call(this, parent, static_cast<int>(context), static_cast<int>(icon), &title, &text, static_cast<int>(buttons.toInt()), static_cast<int>(defaultButton), &handled);
      if (handled) return static_cast<QMessageBox::StandardButton>(given);
    }
    return {};
  }

  //  QMessageBox::StandardButton
  //      QDesignerDialogGuiInterface::message(QWidget *parent, Message
  //      context, QMessageBox::Icon icon, const QString &title, const
  //      QString &text, const QString &informativeText,
  //      QMessageBox::StandardButtons buttons, QMessageBox::StandardButton
  //      defaultButton)
  QMessageBox::StandardButton message(
      QWidget *parent,
      QDesignerDialogGuiInterface::Message context,
      QMessageBox::Icon icon,
      const QString &title,
      const QString &text,
      const QString &informativeText,
      QMessageBox::StandardButtons buttons,
      QMessageBox::StandardButton defaultButton) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerDialogGuiInterfaceCall1 call = reinterpret_cast<CuteQDesignerDialogGuiInterfaceCall1>(taken[1]);
      int given = call(this, parent, static_cast<int>(context), static_cast<int>(icon), &title, &text, &informativeText, static_cast<int>(buttons.toInt()), static_cast<int>(defaultButton), &handled);
      if (handled) return static_cast<QMessageBox::StandardButton>(given);
    }
    return {};
  }

  //  QMessageBox::StandardButton
  //      QDesignerDialogGuiInterface::message(QWidget *parent, Message
  //      context, QMessageBox::Icon icon, const QString &title, const
  //      QString &text, const QString &informativeText, const QString
  //      &detailedText, QMessageBox::StandardButtons buttons,
  //      QMessageBox::StandardButton defaultButton)
  QMessageBox::StandardButton message(
      QWidget *parent,
      QDesignerDialogGuiInterface::Message context,
      QMessageBox::Icon icon,
      const QString &title,
      const QString &text,
      const QString &informativeText,
      const QString &detailedText,
      QMessageBox::StandardButtons buttons,
      QMessageBox::StandardButton defaultButton) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerDialogGuiInterfaceCall2 call = reinterpret_cast<CuteQDesignerDialogGuiInterfaceCall2>(taken[2]);
      int given = call(this, parent, static_cast<int>(context), static_cast<int>(icon), &title, &text, &informativeText, &detailedText, static_cast<int>(buttons.toInt()), static_cast<int>(defaultButton), &handled);
      if (handled) return static_cast<QMessageBox::StandardButton>(given);
    }
    return {};
  }

  //  QString QDesignerDialogGuiInterface::getExistingDirectory(QWidget
  //      *parent, const QString &caption, const QString &dir,
  //      QFileDialog::Options options)
  QString getExistingDirectory(
      QWidget *parent,
      const QString &caption,
      const QString &dir,
      QFileDialog::Options options) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerDialogGuiInterfaceCall3 call = reinterpret_cast<CuteQDesignerDialogGuiInterfaceCall3>(taken[3]);
      QString * given = call(this, parent, &caption, &dir, static_cast<int>(options.toInt()), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerDialogGuiInterface::getOpenFileName(QWidget *parent,
  //      const QString &caption, const QString &dir, const QString
  //      &filter, QString *selectedFilter, QFileDialog::Options options)
  QString getOpenFileName(
      QWidget *parent,
      const QString &caption,
      const QString &dir,
      const QString &filter,
      QString *selectedFilter,
      QFileDialog::Options options) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerDialogGuiInterfaceCall4 call = reinterpret_cast<CuteQDesignerDialogGuiInterfaceCall4>(taken[4]);
      QString * given = call(this, parent, &caption, &dir, &filter, selectedFilter, static_cast<int>(options.toInt()), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerDialogGuiInterface::getOpenImageFileName(QWidget
  //      *parent, const QString &caption, const QString &dir, const
  //      QString &filter, QString *selectedFilter, QFileDialog::Options
  //      options)
  QString getOpenImageFileName(
      QWidget *parent,
      const QString &caption,
      const QString &dir,
      const QString &filter,
      QString *selectedFilter,
      QFileDialog::Options options) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerDialogGuiInterfaceCall5 call = reinterpret_cast<CuteQDesignerDialogGuiInterfaceCall5>(taken[5]);
      QString * given = call(this, parent, &caption, &dir, &filter, selectedFilter, static_cast<int>(options.toInt()), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesignerDialogGuiInterface::getOpenImageFileName(parent, caption, dir, filter, selectedFilter, options);
  }

  //  QString QDesignerDialogGuiInterface::getSaveFileName(QWidget *parent,
  //      const QString &caption, const QString &dir, const QString
  //      &filter, QString *selectedFilter, QFileDialog::Options options)
  QString getSaveFileName(
      QWidget *parent,
      const QString &caption,
      const QString &dir,
      const QString &filter,
      QString *selectedFilter,
      QFileDialog::Options options) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerDialogGuiInterfaceCall6 call = reinterpret_cast<CuteQDesignerDialogGuiInterfaceCall6>(taken[6]);
      QString * given = call(this, parent, &caption, &dir, &filter, selectedFilter, static_cast<int>(options.toInt()), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
};

//  QDesignerDialogGuiInterface::~QDesignerDialogGuiInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerDialogGuiInterfaceD1Ev(
    QDesignerDialogGuiInterface *self) {
  delete self;
}

//  QMessageBox::StandardButton QDesignerDialogGuiInterface::message(QWidget
//      *parent, Message context, QMessageBox::Icon icon, const QString
//      &title, const QString &text, QMessageBox::StandardButtons buttons,
//      QMessageBox::StandardButton defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7MessageEN11QMessageBox4IconERK7QStringS7_6QFlagsINS3_14StandardButtonEES9_(
    QDesignerDialogGuiInterface *self,
    QWidget *parent,
    QDesignerDialogGuiInterface::Message context,
    QMessageBox::Icon icon,
    const QString *title,
    const QString *text,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return self->message(
      parent,
      context,
      icon,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

//  QMessageBox::StandardButton QDesignerDialogGuiInterface::message(QWidget
//      *parent, Message context, QMessageBox::Icon icon, const QString
//      &title, const QString &text, const QString &informativeText,
//      QMessageBox::StandardButtons buttons, QMessageBox::StandardButton
//      defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7MessageEN11QMessageBox4IconERK7QStringS7_S7_6QFlagsINS3_14StandardButtonEES9_(
    QDesignerDialogGuiInterface *self,
    QWidget *parent,
    QDesignerDialogGuiInterface::Message context,
    QMessageBox::Icon icon,
    const QString *title,
    const QString *text,
    const QString *informativeText,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return self->message(
      parent,
      context,
      icon,
      *title,
      *text,
      *informativeText,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

//  QMessageBox::StandardButton QDesignerDialogGuiInterface::message(QWidget
//      *parent, Message context, QMessageBox::Icon icon, const QString
//      &title, const QString &text, const QString &informativeText, const
//      QString &detailedText, QMessageBox::StandardButtons buttons,
//      QMessageBox::StandardButton defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7MessageEN11QMessageBox4IconERK7QStringS7_S7_S7_6QFlagsINS3_14StandardButtonEES9_(
    QDesignerDialogGuiInterface *self,
    QWidget *parent,
    QDesignerDialogGuiInterface::Message context,
    QMessageBox::Icon icon,
    const QString *title,
    const QString *text,
    const QString *informativeText,
    const QString *detailedText,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return self->message(
      parent,
      context,
      icon,
      *title,
      *text,
      *informativeText,
      *detailedText,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

//  QString QDesignerDialogGuiInterface::getExistingDirectory(QWidget
//      *parent, const QString &caption, const QString &dir,
//      QFileDialog::Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDesignerDialogGuiInterface20getExistingDirectoryEP7QWidgetRK7QStringS4_6QFlagsIN11QFileDialog6OptionEE(
    QDesignerDialogGuiInterface *self,
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    int options) {
  return new QString(
      self->getExistingDirectory(
          parent,
          *caption,
          *dir,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QString QDesignerDialogGuiInterface::getOpenFileName(QWidget *parent,
//      const QString &caption, const QString &dir, const QString &filter,
//      QString *selectedFilter, QFileDialog::Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDesignerDialogGuiInterface15getOpenFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE(
    QDesignerDialogGuiInterface *self,
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QString(
      self->getOpenFileName(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QString QDesignerDialogGuiInterface::getOpenImageFileName(QWidget
//      *parent, const QString &caption, const QString &dir, const QString
//      &filter, QString *selectedFilter, QFileDialog::Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDesignerDialogGuiInterface20getOpenImageFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE(
    QDesignerDialogGuiInterface *self,
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QString(
      self->getOpenImageFileName(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QStringList QDesignerDialogGuiInterface::getOpenFileNames(QWidget
//      *parent, const QString &caption, const QString &dir, const QString
//      &filter, QString *selectedFilter, QFileDialog::Options options)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN27QDesignerDialogGuiInterface16getOpenFileNamesEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE(
    QDesignerDialogGuiInterface *self,
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QList<QString>(
      self->getOpenFileNames(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QStringList QDesignerDialogGuiInterface::getOpenImageFileNames(QWidget
//      *parent, const QString &caption, const QString &dir, const QString
//      &filter, QString *selectedFilter, QFileDialog::Options options)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN27QDesignerDialogGuiInterface21getOpenImageFileNamesEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE(
    QDesignerDialogGuiInterface *self,
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QList<QString>(
      self->getOpenImageFileNames(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QString QDesignerDialogGuiInterface::getSaveFileName(QWidget *parent,
//      const QString &caption, const QString &dir, const QString &filter,
//      QString *selectedFilter, QFileDialog::Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDesignerDialogGuiInterface15getSaveFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE(
    QDesignerDialogGuiInterface *self,
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QString(
      self->getSaveFileName(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  a Python function taken by a CuteQDesignerDialogGuiInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerDialogGuiInterface(
    QDesignerDialogGuiInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerDialogGuiInterface *>(self)->take(key, call);
}

//  QString QDesignerDialogGuiInterface::getOpenImageFileName(QWidget
//      *parent, const QString &caption, const QString &dir, const QString
//      &filter, QString *selectedFilter, QFileDialog::Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN27QDesignerDialogGuiInterface20getOpenImageFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE(
    QDesignerDialogGuiInterface *self,
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QString(
      self->QDesignerDialogGuiInterface::getOpenImageFileName(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}
