//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/dialoggui_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/dialoggui_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A qdesigner_internal::DialogGui that Python can take functions over in. Every qdesigner_internal::DialogGui
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*Cuteqdesigner_internal_DialogGuiCall0)(const void *, QWidget *, int, int, const QString *, const QString *, int, int, int *);
typedef int (*Cuteqdesigner_internal_DialogGuiCall1)(const void *, QWidget *, int, int, const QString *, const QString *, const QString *, int, int, int *);
typedef int (*Cuteqdesigner_internal_DialogGuiCall2)(const void *, QWidget *, int, int, const QString *, const QString *, const QString *, const QString *, int, int, int *);
typedef QString * (*Cuteqdesigner_internal_DialogGuiCall3)(const void *, QWidget *, const QString *, const QString *, int, int *);
typedef QString * (*Cuteqdesigner_internal_DialogGuiCall4)(const void *, QWidget *, const QString *, const QString *, const QString *, QString *, int, int *);
typedef QString * (*Cuteqdesigner_internal_DialogGuiCall5)(const void *, QWidget *, const QString *, const QString *, const QString *, QString *, int, int *);
typedef QString * (*Cuteqdesigner_internal_DialogGuiCall6)(const void *, QWidget *, const QString *, const QString *, const QString *, QString *, int, int *);
class Cuteqdesigner_internal_DialogGui : public qdesigner_internal::DialogGui {
public:
  using qdesigner_internal::DialogGui::DialogGui;
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
    if (!std::strcmp(key, "_ZN27QDesignerDialogGuiInterface15getSaveFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerDialogGuiInterface20getOpenImageFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QMessageBox::StandardButton
  //      qdesigner_internal::DialogGui::message(QWidget *parent, Message
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
      Cuteqdesigner_internal_DialogGuiCall0 call = reinterpret_cast<Cuteqdesigner_internal_DialogGuiCall0>(taken[0]);
      int given = call(this, parent, static_cast<int>(context), static_cast<int>(icon), &title, &text, static_cast<int>(buttons.toInt()), static_cast<int>(defaultButton), &handled);
      if (handled) return static_cast<QMessageBox::StandardButton>(given);
    }
    return qdesigner_internal::DialogGui::message(parent, context, icon, title, text, buttons, defaultButton);
  }

  //  QMessageBox::StandardButton
  //      qdesigner_internal::DialogGui::message(QWidget *parent, Message
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
      Cuteqdesigner_internal_DialogGuiCall1 call = reinterpret_cast<Cuteqdesigner_internal_DialogGuiCall1>(taken[1]);
      int given = call(this, parent, static_cast<int>(context), static_cast<int>(icon), &title, &text, &informativeText, static_cast<int>(buttons.toInt()), static_cast<int>(defaultButton), &handled);
      if (handled) return static_cast<QMessageBox::StandardButton>(given);
    }
    return qdesigner_internal::DialogGui::message(parent, context, icon, title, text, informativeText, buttons, defaultButton);
  }

  //  QMessageBox::StandardButton
  //      qdesigner_internal::DialogGui::message(QWidget *parent, Message
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
      Cuteqdesigner_internal_DialogGuiCall2 call = reinterpret_cast<Cuteqdesigner_internal_DialogGuiCall2>(taken[2]);
      int given = call(this, parent, static_cast<int>(context), static_cast<int>(icon), &title, &text, &informativeText, &detailedText, static_cast<int>(buttons.toInt()), static_cast<int>(defaultButton), &handled);
      if (handled) return static_cast<QMessageBox::StandardButton>(given);
    }
    return qdesigner_internal::DialogGui::message(parent, context, icon, title, text, informativeText, detailedText, buttons, defaultButton);
  }

  //  QString qdesigner_internal::DialogGui::getExistingDirectory(QWidget
  //      *parent, const QString &caption, const QString &dir,
  //      QFileDialog::Options options)
  QString getExistingDirectory(
      QWidget *parent,
      const QString &caption,
      const QString &dir,
      QFileDialog::Options options) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_DialogGuiCall3 call = reinterpret_cast<Cuteqdesigner_internal_DialogGuiCall3>(taken[3]);
      QString * given = call(this, parent, &caption, &dir, static_cast<int>(options.toInt()), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return qdesigner_internal::DialogGui::getExistingDirectory(parent, caption, dir, options);
  }

  //  QString qdesigner_internal::DialogGui::getOpenFileName(QWidget
  //      *parent, const QString &caption, const QString &dir, const
  //      QString &filter, QString *selectedFilter, QFileDialog::Options
  //      options)
  QString getOpenFileName(
      QWidget *parent,
      const QString &caption,
      const QString &dir,
      const QString &filter,
      QString *selectedFilter,
      QFileDialog::Options options) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_DialogGuiCall4 call = reinterpret_cast<Cuteqdesigner_internal_DialogGuiCall4>(taken[4]);
      QString * given = call(this, parent, &caption, &dir, &filter, selectedFilter, static_cast<int>(options.toInt()), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return qdesigner_internal::DialogGui::getOpenFileName(parent, caption, dir, filter, selectedFilter, options);
  }

  //  QString qdesigner_internal::DialogGui::getSaveFileName(QWidget
  //      *parent, const QString &caption, const QString &dir, const
  //      QString &filter, QString *selectedFilter, QFileDialog::Options
  //      options)
  QString getSaveFileName(
      QWidget *parent,
      const QString &caption,
      const QString &dir,
      const QString &filter,
      QString *selectedFilter,
      QFileDialog::Options options) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_DialogGuiCall5 call = reinterpret_cast<Cuteqdesigner_internal_DialogGuiCall5>(taken[5]);
      QString * given = call(this, parent, &caption, &dir, &filter, selectedFilter, static_cast<int>(options.toInt()), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return qdesigner_internal::DialogGui::getSaveFileName(parent, caption, dir, filter, selectedFilter, options);
  }

  //  QString qdesigner_internal::DialogGui::getOpenImageFileName(QWidget
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
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_DialogGuiCall6 call = reinterpret_cast<Cuteqdesigner_internal_DialogGuiCall6>(taken[6]);
      QString * given = call(this, parent, &caption, &dir, &filter, selectedFilter, static_cast<int>(options.toInt()), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return qdesigner_internal::DialogGui::getOpenImageFileName(parent, caption, dir, filter, selectedFilter, options);
  }
};

//  a Python function taken by a Cuteqdesigner_internal_DialogGui, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_DialogGui(
    qdesigner_internal::DialogGui *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_DialogGui *>(self)->take(key, call);
}

//  QMessageBox::StandardButton
//      qdesigner_internal::DialogGui::message(QWidget *parent, Message
//      context, QMessageBox::Icon icon, const QString &title, const QString
//      &text, QMessageBox::StandardButtons buttons,
//      QMessageBox::StandardButton defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_own_ZN18qdesigner_internal9DialogGui7messageEP7QWidgetN27QDesignerDialogGuiInterface7MessageEN11QMessageBox4IconERK7QStringS9_6QFlagsINS5_14StandardButtonEESB_(
    qdesigner_internal::DialogGui *self,
    QWidget *parent,
    QDesignerDialogGuiInterface::Message context,
    QMessageBox::Icon icon,
    const QString *title,
    const QString *text,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return self->qdesigner_internal::DialogGui::message(
      parent,
      context,
      icon,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

//  QMessageBox::StandardButton
//      qdesigner_internal::DialogGui::message(QWidget *parent, Message
//      context, QMessageBox::Icon icon, const QString &title, const QString
//      &text, const QString &informativeText, QMessageBox::StandardButtons
//      buttons, QMessageBox::StandardButton defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_own_ZN18qdesigner_internal9DialogGui7messageEP7QWidgetN27QDesignerDialogGuiInterface7MessageEN11QMessageBox4IconERK7QStringS9_S9_6QFlagsINS5_14StandardButtonEESB_(
    qdesigner_internal::DialogGui *self,
    QWidget *parent,
    QDesignerDialogGuiInterface::Message context,
    QMessageBox::Icon icon,
    const QString *title,
    const QString *text,
    const QString *informativeText,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return self->qdesigner_internal::DialogGui::message(
      parent,
      context,
      icon,
      *title,
      *text,
      *informativeText,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

//  QMessageBox::StandardButton
//      qdesigner_internal::DialogGui::message(QWidget *parent, Message
//      context, QMessageBox::Icon icon, const QString &title, const QString
//      &text, const QString &informativeText, const QString &detailedText,
//      QMessageBox::StandardButtons buttons, QMessageBox::StandardButton
//      defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_own_ZN18qdesigner_internal9DialogGui7messageEP7QWidgetN27QDesignerDialogGuiInterface7MessageEN11QMessageBox4IconERK7QStringS9_S9_S9_6QFlagsINS5_14StandardButtonEESB_(
    qdesigner_internal::DialogGui *self,
    QWidget *parent,
    QDesignerDialogGuiInterface::Message context,
    QMessageBox::Icon icon,
    const QString *title,
    const QString *text,
    const QString *informativeText,
    const QString *detailedText,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return self->qdesigner_internal::DialogGui::message(
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

//  QString qdesigner_internal::DialogGui::getExistingDirectory(QWidget
//      *parent, const QString &caption, const QString &dir,
//      QFileDialog::Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN18qdesigner_internal9DialogGui20getExistingDirectoryEP7QWidgetRK7QStringS5_6QFlagsIN11QFileDialog6OptionEE(
    qdesigner_internal::DialogGui *self,
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    int options) {
  return new QString(
      self->qdesigner_internal::DialogGui::getExistingDirectory(
          parent,
          *caption,
          *dir,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QString qdesigner_internal::DialogGui::getOpenFileName(QWidget *parent,
//      const QString &caption, const QString &dir, const QString &filter,
//      QString *selectedFilter, QFileDialog::Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN18qdesigner_internal9DialogGui15getOpenFileNameEP7QWidgetRK7QStringS5_S5_PS3_6QFlagsIN11QFileDialog6OptionEE(
    qdesigner_internal::DialogGui *self,
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QString(
      self->qdesigner_internal::DialogGui::getOpenFileName(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QString qdesigner_internal::DialogGui::getSaveFileName(QWidget *parent,
//      const QString &caption, const QString &dir, const QString &filter,
//      QString *selectedFilter, QFileDialog::Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN18qdesigner_internal9DialogGui15getSaveFileNameEP7QWidgetRK7QStringS5_S5_PS3_6QFlagsIN11QFileDialog6OptionEE(
    qdesigner_internal::DialogGui *self,
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QString(
      self->qdesigner_internal::DialogGui::getSaveFileName(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QString qdesigner_internal::DialogGui::getOpenImageFileName(QWidget
//      *parent, const QString &caption, const QString &dir, const QString
//      &filter, QString *selectedFilter, QFileDialog::Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN18qdesigner_internal9DialogGui20getOpenImageFileNameEP7QWidgetRK7QStringS5_S5_PS3_6QFlagsIN11QFileDialog6OptionEE(
    qdesigner_internal::DialogGui *self,
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QString(
      self->qdesigner_internal::DialogGui::getOpenImageFileName(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}
